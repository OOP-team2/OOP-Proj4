from models.Action import Action
from models.Player import Player
from exceptions.Exit import Exit
from exceptions.Die import Die
from views.ViewInterface import ViewInterface
from services.Dealer import Dealer

# This is a Class for a round of a game
class Round:
    # constructor for a Round instance
    def __init__(self, default_bet: int, dealer: Dealer, view_interface: ViewInterface) -> None:
        # member variable for saving winner id
        self.winner_id: int = -1
        # member variable for dealer of a round
        self.dealer: Dealer = dealer
        # member variable for total bet of a round
        self.total_bet: int = 0
        # member variable for a default bet of a round
        self.default_bet: int = default_bet
        # member variable for user interface
        self.__view_interface: ViewInterface = view_interface
        # member variable for saving how many turns are done in a round
        self.rounds_done_in: int = 0
        # member variable for saving the user had call action
        self.did_call: [] = [False,False]
        # member variable for saving who is the first turn
        self.first_turn: int = 0
        # member variable for saving the bets of a round
        self.bets: [] = []
    
    # member function for adding a winner of a round
    def add_winner(self, winner: Player) -> None:
        self.winner = winner

    # member function for restargin a round when a draw happens
    def restart_round(self, players) -> None:
        round_turn: int = self.rounds_done_in
        self.first_turn = (self.first_turn+1)%2
        turn = self.first_turn
        self.did_call.clear()
        self.did_call.extend([False, False])
        self.__view_interface.display_total_betting(sum(self.bets))
        try:
            while self.__is_not_round_end():
                if turn % 2 == self.first_turn:
                    round_turn += 1
                actions = players[turn].actions(round_turn, self.first_turn, self.did_call[turn])

                if players[turn].get_id() == 0:
                    self.__view_interface.display_menu([action.name for action in actions])

                action: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action = actions[user_input]
                else:
                    action = players[turn].auto_action()
                turn = self.__take_action(action, turn, players[turn])
        except Die as e:
            self.winner_id = (int(str(e))+1)%2
        finally:
            self.total_bet = sum(self.bets)
            players[self.winner_id].take(self.total_bet)
            self.rounds_done_in = round_turn

    # member function for staring a round
    def start_round(self, first_turn: int, players: list) -> None:
        self.did_call.clear()
        self.did_call.extend([False,False])
        self.first_turn = first_turn
        self.bets = [self.default_bet, self.default_bet]
        round_turn: int = 0
        turn = first_turn

        self.__view_interface.display_total_betting(sum(self.bets))

        try:
            while self.__is_not_round_end():
                if turn % 2 == first_turn:
                    round_turn += 1

                actions = players[turn].actions(round_turn, first_turn, self.did_call[turn])

                if players[turn].get_id() == 0:
                    self.__view_interface.display_menu([action.name for action in actions])

                action: Action = None
                if players[turn].get_id() == 0:
                    user_input = self.__view_interface.display_input()
                    action = actions[user_input]
                else:
                    action = players[turn].auto_action()
                turn = self.__take_action(action, turn, players[turn])  
        except Die as e:
            self.winner_id = (int(str(e))+1)%2
        finally:
            self.total_bet = sum(self.bets)
            players[self.winner_id].take(self.total_bet)
            self.rounds_done_in = round_turn

    # member function for check whether a round is ended
    def __is_not_round_end(self):
        return False in self.did_call

    # member function for taking a player action
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
                self.bets[turn] += player.get_stakes()
                player.bet(player.get_stakes())
            else:
                self.bets[turn] += bet_amount
                player.bet(bet_amount)
        elif action == Action.HALF:
            half_bet_amount: int = max(self.bets)
            if half_bet_amount > player.get_stakes():
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