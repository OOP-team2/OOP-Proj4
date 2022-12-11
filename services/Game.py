import time
from models.Player import Player
from services.Dealer import Dealer
from models.AutoPlayer import AutoPlayer
from services.Round import Round
from exceptions.Exit import Exit
from views.ViewInterface import ViewInterface

# This is a Class for a Game
# The User plays first always
class Game:
    # constructor for a Game instance
    def __init__(self):
        # member variable for save rounds
        self.rounds: list = []
        # member variable for the winner of game
        self.winner: Player = None
        # member variable for total bet
        self.total_bet: int = 0
        # member variable for the dealer of game
        self.dealer: Dealer = None
        # member variable for the computer player
        self.computer_player = None
        # member variable for the player(user)
        self.player = None
        # member variable for the user interface
        self.view_interface: ViewInterface = ViewInterface()

    # member function to start a game
    def start_game(self) -> None:
        self.view_interface.display_background()
        self.view_interface.display_menu()
        self.view_interface.display_rounds()

        self.dealer = Dealer()

        self.player = Player(10000)
        self.computer_player = AutoPlayer(10000)

        self.view_interface.display_player(self.player.get_id(), self.player.get_stakes())
        self.view_interface.display_player(self.computer_player.get_id(), self.computer_player.get_stakes())

        self.view_interface.display_betting(0)
        self.view_interface.display_total_betting(0)

        game_turn: int = 0
        rounds: int = 1
        try:
            while not self.dealer.check_game_ended(self.player, self.computer_player):
                self.view_interface.display_rounds(rounds)

                if self.player.get_stakes() < 1000 or self.computer_player.get_stakes() < 1000:
                    self.default_bet = min(self.player.get_stakes(), self.computer_player.get_stakes())
                else:
                    self.default_bet = 1000

                game_round: Round = Round(self.default_bet, self.dealer, self.view_interface)

                self.dealer.distribute_cards(self.player, self.computer_player)

                self.view_interface.display_hand(self.player.get_id(), self.player.get_hand(), front=True)
                self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=False)
                
                self.player.bet(self.default_bet)
                self.computer_player.bet(self.default_bet)
                self.view_interface.display_player(self.player.get_id(), self.player.get_stakes())
                self.view_interface.display_player(self.computer_player.get_id(), self.computer_player.get_stakes())

                game_round.start_round(game_turn, [self.player, self.computer_player])

                round_winner: Player = self.dealer.announce_winner(self.player, self.computer_player, False)

                if round_winner.get_stakes() == -1:
                    self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=True)
                    self.dealer.distribute_cards(self.player, self.computer_player)
                    self.view_interface.display_hand(self.player.get_id(), self.player.get_hand(), front=True)
                    self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=False)
                    game_round.restart_round([self.player, self.computer_player])
                    round_winner = self.dealer.announce_winner(self.player, self.computer_player, True)

                self.view_interface.display_hand(self.computer_player.get_id(), self.computer_player.get_hand(), front=True)
                game_round.add_winner(round_winner)
                rounds += 1

                self.rounds.append(game_round)
                game_turn = 1 if game_turn == 0 else 0

                time.sleep(3)

            self.winner = self.player if self.player.get_stakes() > self.computer_player.get_stakes() else self.computer_player
        except Exit as e:
            self.winner = self.player if str(e) == '1' else self.computer_player
        finally:
            self.total_bet = self.winner.get_stakes()
            self.view_interface.display_winner(self.winner.get_id())
