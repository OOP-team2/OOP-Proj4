# 한 라운드를 책임지는 클래스입니다.
from models.Action import Action
from models.Player import Player
from exceptions.Exit import Exit
from exceptions.Die import Die
from views.ViewInterface import ViewInterface

class Round:
    def __init__(self, default_bet: int, dealer, view_interface: ViewInterface) -> None:
        self.winner_id: int = -1
        self.dealer = dealer
        self.total_bet = 0
        self.default_bet = default_bet
        self.bet_per_round: int = 0
        self.__view_interface: ViewInterface = view_interface
        self.rounds_done: int = 0
        self.did_call = [False,False]
        self.first_turn: int = 0
        self.bets = []
        
    def add_winner(self, winner: Player) -> None:
        self.winner = winner

    def restart_round(self, players):
        all_set: bool = False
        round_turn: int = self.rounds_done
        self.first_turn = (self.first_turn+1)%2
        turn = self.first_turn
        available_actions = [action for action in Action]
        self.did_call.clear()
        self.did_call.extend([False, False])
        self.__view_interface.display_total_betting(sum(self.bets))
        # 한 라운드를 시작하는 루프
        try:
            while not all_set:
                # 한 턴씩 진행합니다.
                # 둘 중에 하나가 죽으면 현재 라운드의 총 베팅 금액은 죽지않은쪽으로 갑니다.
                # 둘중에 하나라도 게임을 종료하면(exit) 바로 함수를 종료합니다.
                actions1 = players[turn].actions(round_turn, self.first_turn, self.did_call[turn])
                # 선택할 수 있는 액션만 보여줍니다.
                self.__view_interface.display_menu([action.name for action in actions1])

                # 플레이어만 액션을 입력받습니다.
                action1: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action1 = actions1[user_input]
                else:
                    action1 = players[turn].auto_action()
                turn = self.__take_action(action1, turn, players[turn])
                
                self.__view_interface.display_total_betting(sum(self.bets))
                self.__view_interface.display_player(players[turn].get_id(), players[turn].get_stakes())

                # 엑싯한 경우, 그냥 게임을 종료하고 게임의 승자는 상대편이 됩니다.
                # 예외를 발생시키고 패자 메시지를 담습니다.
                actions2: Action = players[turn].actions(round_turn, self.first_turn, self.did_call[turn])
                # 선택할 수 있는 액션만 보여줍니다.
                self.__view_interface.display_menu([action.name for action in actions2])
                # 액션을 입력받습니다.
                action2: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action2 = actions2[user_input]
                else:
                    action2 = players[turn].auto_action()
                turn = self.__take_action(action2, turn, players[turn])

                self.__view_interface.display_total_betting(sum(self.bets))
                self.__view_interface.display_player(players[turn].get_id(), players[turn].get_stakes())
                
                if self.__is_round_end(action1, action2):
                    all_set = True
                round_turn += 1
        except Die as e:
            # 죽는 행동이 나오면 여기서 캐치해서 라운드를 끝냅니다.
            self.winner_id = (int(str(e))+1)%2
        finally:
            self.total_bet = sum(self.bets)
            players[self.winner_id].take(self.total_bet)
            self.rounds_done = round_turn

    def start_round(self, first_turn: int, players: list) -> int:
        # 라운드가 시작되면 턴을 돌아가면서 베팅을합니다.
        # 라운드가 끝나면 컴퓨터와 플레이어는 자신의 패를 공개하고
        # 가장 높은 밸류를 가진 패가 이깁니다.

        # 매 라운드에서
        # 첫턴이 나라면 내가 콜은 못하고 다이나 하프
        # 그리고 다음턴이 컴퓨터가 되고, 다이, 콜, 하프 가능
        # 그리고 내 턴이 되면 다이 콜 하프 가능
        # 그리고 콜 콜 하면 끝남
        # 라운드 내에서 베팅을 반복하는 것 필요
        # 베팅 금액을 정합니다.

        # 라운드가 시작하기 전에 패를 확인하고 죽을지 안죽을지를 결정합니다.

        # 만약 한명이 다이 -> 다른 한명이 베팅 금액 다 가져가고 라운드 종료
        # 만약 콜 콜 -> 1. 베팅 금액이 같은 경우 2. 올인을 하는 경우
        # -> 승자 판별하고 승자에게 돈주고 라운드 종료
        self.did_call.clear()
        self.did_call.extend([False,False])
        self.first_turn = first_turn
        self.bets = [self.default_bet, self.default_bet]
        round_turn: int = 0
        turn = first_turn
        available_actions = [action for action in Action]

        self.__view_interface.display_total_betting(sum(self.bets))
        # 한 라운드를 시작하는 루프
        try:
            while False in self.did_call:
                round_turn += 1
                # 한 턴씩 진행합니다.
                # 둘 중에 하나가 죽으면 현재 라운드의 총 베팅 금액은 죽지않은쪽으로 갑니다.
                # 둘중에 하나라도 게임을 종료하면(exit) 바로 함수를 종료합니다.
                actions1 = players[turn].actions(round_turn, first_turn, self.did_call[turn])
                # 선택할 수 있는 액션만 보여줍니다.
                if players[turn].get_id() == 0:
                    self.__view_interface.display_menu([action.name for action in actions1])

                # 플레이어만 액션을 입력받습니다.
                action1: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action1 = actions1[user_input]
                else:
                    action1 = players[turn].auto_action()
                turn = self.__take_action(action1, turn, players[turn])
                
                if not False in self.did_call:
                    break

                # 엑싯한 경우, 그냥 게임을 종료하고 게임의 승자는 상대편이 됩니다.
                # 예외를 발생시키고 패자 메시지를 담습니다.
                actions2: Action = players[turn].actions(round_turn, first_turn, self.did_call[turn])
                # 선택할 수 있는 액션만 보여줍니다.
                if players[turn].get_id() == 0:
                    self.__view_interface.display_menu([action.name for action in actions2])
                # 액션을 입력받습니다.
                action2: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action2 = actions2[user_input]
                else:
                    action2 = players[turn].auto_action()
                turn = self.__take_action(action2, turn, players[turn])

                if not False in self.did_call:
                    break
        except Die as e:
            # 죽는 행동이 나오면 여기서 캐치해서 라운드를 끝냅니다.
            self.winner_id = (int(str(e))+1)%2
        finally:
            self.total_bet = sum(self.bets)
            players[self.winner_id].take(self.total_bet)
            self.rounds_done = round_turn

    def __is_round_end(self, action1: Action, action2: Action):
        is_round_end = False
        if action1 == Action.CALL and action2 == Action.CALL:
            is_round_end = True
        return is_round_end

    def __take_action(self, action: Action, turn: int, player: Player) -> int:
        if action == Action.EXIT:
            self.total_bet = sum(self.bets)
            raise Exit(str(player.get_id()))
        elif action == Action.DIE:
            raise Die(str(player.get_id()))
        elif action == Action.CALL:
            self.did_call[turn] = True
            bet_amount: int = self.bets[(turn+1)%2] - self.bets[turn]
            if bet_amount > player.get_stakes():
                # 가진 돈보다 콜 해야하는 금액이 많으면 올인합니다.
                self.bets[turn] += player.get_stakes()
                player.bet(player.get_stakes())
            else:
                self.bets[turn] += bet_amount
                player.bet(bet_amount)
        elif action == Action.HALF:
            # 가진 돈보다 하프 해야하는 금액이 많으면 올인합니다.
            half_bet_amount: int = max(self.bets)
            if half_bet_amount > player.get_stakes():
                # 가진 돈보다 하프 해야하는 금액이 많으면 올인합니다.
                self.bets[turn] += player.get_stakes()
                player.bet(player.get_stakes())
                self.did_call[turn] = turn
            else:
                self.bets[turn] += half_bet_amount
                player.bet(half_bet_amount)

        self.__view_interface.display_player(player.get_id(), player.get_stakes())
        self.__view_interface.display_betting(self.bets[0])
        self.__view_interface.display_total_betting(sum(self.bets))
        return 1 if turn == 0 else 0