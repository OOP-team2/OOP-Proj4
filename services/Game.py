import time

from models.Player import Player
from models.Dealer import Dealer
from models.AutoPlayer import AutoPlayer
from services.Round import Round
from exceptions.Exit import Exit
from views.ViewInterface import ViewInterface

# 한 게임을 책임지는 클래스입니다.
class Game:
    def __init__(self):
        self.rounds: list = []
        self.winner: Player = None
        self.totalBet: int = 0
        self.dealer: Dealer = None
        # 플레이어들 중 첫번째는 항상 컴퓨터입니다.
        self.computer_player = None
        self.player = None
        # 패를 보여줄 뷰를 가집니다.
        self.view_interface: ViewInterface = ViewInterface()
    def start_game(self) -> None:
        # 초기 화면을 출력합니다.
        self.view_interface.display_background()
        self.view_interface.display_menu()
        self.view_interface.display_rounds()

        # 딜러를 초기화합니다.
        self.dealer = Dealer()
        # 판돈을 정합니다. -> 라운드마다 처음에 고정인데 -> 베팅을 하면 커진다
        # 예) 1000원 -> 플레이어당 천원씩 깔림
        # 플레이어와 컴퓨터 플레이어를 생성합니다.
        self.player = Player(10000)
        self.computer_player = AutoPlayer(10000)

        self.view_interface.display_player(self.player.get_id(), self.player.get_stakes())
        self.view_interface.display_player(self.computer_player.get_id(), self.computer_player.get_stakes())

        self.view_interface.display_betting(0)
        self.view_interface.display_total_betting(0)

        # 게임이 끝나지 않았으면 게임을 계속합니다.
        # 매번 한 라운드를 생성합니다.
        # 종료조건: 기본 베팅 금액보다 돈이 적으면 게임 종료
        # 라운드마다 플레이어와 컴퓨터가 각자 베팅한 금액의 총합에 대한 정보가 어딘가 있어야한다.(라운드, 딜러)
        # -> 라운드로 합시다.
        # 첫 턴은 항상 플레이어입니다. game_turn이 1이면 플레이어 턴, 0이면 컴퓨터 턴입니다.
        game_turn: int = 1
        rounds: int = 1
        try:
            while not self.dealer.check_game_ended(self.player, self.computer_player):
                self.view_interface.display_rounds(rounds)
                # 기본 베팅 금액을 정합니다. 둘 다 천원이상 있으면 천원,
                # 어느 한쪽이라도 돈이 모자라면 모자란쪽의 전 재산이 최소 베팅 금액이 됩니다.
                if self.player.get_stakes() < 1000 or self.computer_player.get_stakes() < 1000:
                    self.default_bet = min(self.player.get_stakes(), self.computer_player.get_stakes())
                else:
                    self.default_bet = 1000

                game_round: Round = Round(self.default_bet, self.dealer, self.view_interface)
                # 라운드가 생성되면 딜러가 패를 분배합니다.
                self.dealer.distribute_cards(self.player, self.computer_player)

                # 패가 분배되면 플레이어는 패를 확인합니다.
                # 패는 콘솔창에 출력합니다.
                self.view_interface.display_hand(self.player.get_id(), self.player.get_hand(), front=True)
                self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=True)
                
                # 라운드가 시작됩니다. 베팅이 반복됩니다.
                self.view_interface.display_player(self.player.get_id(), self.player.get_stakes())
                self.view_interface.display_player(self.computer_player.get_id(), self.computer_player.get_stakes())
                game_round.start_round(game_turn, [self.computer_player, self.player])

                # 딜러가 승자를 판별합니다.
                round_winner: Player = self.dealer.announce_winner(self.player, self.computer_player)

                # 라운드에 승자를 추가합니다.
                # 라운드 승자와 얻은 금액을 입력합니다.
                self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=True)
                game_round.add_winner(round_winner)
                rounds += 1
                # 라운드를 진행된 라운드에 추가하는 것은 라운드가 끝나고 마지막에 합니다.
                self.rounds.append(game_round)
                game_turn += 1
                game_turn %= 2
                # 시간 간격을 둡니다. 3초 정도
                time.sleep(3)
            # 게임이 끝나면 승자를 판별합니다.
            # 가진 돈이 더 많은 쪽이 승자입니다.
            self.winner = self.player if self.player.get_stakes() > self.computer_player.get_stakes() else self.computer_player
        except Exit:
            self.winner = self.player if Exit.looser == 0 else self.computer_player
        finally:
            # 게임이 끝나면 승자와 최종 승리 금액을 출력합니다.
            self.view_interface.display_winner(self.winner.get_id())
    def end_game(self) -> None:
        self.is_game_ended = True

    def create_player(self, bet_money: int) -> Player:
        return Player(bet_money)

    def show_opponent_hands(self) -> None:
        pass

    def display_player(self) -> None:
        pass

    def display_hand(self):
        pass
