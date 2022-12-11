from views.BackgroundView import *
from views.HandView import *
from views.PlayerView import *
from views.BettingView import *
from views.WinnerView import *
from console.screen import sc

# Interface of overall views
class ViewInterface:

    def __init__(self):
        # initializing views
        self.__bg = BackgroundView()
        self.__hv = HandView()
        self.__pv = PlayerView()
        self.__bv = BettingView()
        self.__wv = WinnerView()

    # from BackgroundView
    def display_background(self):
        self.__bg.display_background()

    # from BackgroundView
    def display_menu(self, actions: [str] = ("EXIT", "DIE", "CALL", "HALF")):
        self.__clear(POS_MENU, (HEIGHT_WINDOW, WIDTH_WINDOW))
        self.__bg.display_menu(actions)

    # from BackgroundView
    def display_rounds(self, rounds: int = 1):
        self.__clear(POS_ROUNDS, (POS_ROUNDS[0] + WORD_HEIGHT, POS_ROUNDS[1] + 2 * NUM_WIDTH))
        self.__bg.display_rounds(rounds)

    # from BackgroundView
    def display_input(self) -> int:
        return self.__bg.display_input()

    # from HandView
    def display_hand(self, player: int, hand: dict = (0, 0), front: bool = True):
        self.__hv.display_hand(player, hand, front)

    # from PlayerView
    def display_player(self, player: int, stakes: int = 0):
        if player == 0:
            lu, rb = POS_PLAYER, (POS_PLAYER[0] + 21, POS_PLAYER[1] + 62)
        else:
            lu, rb = POS_COMPUTER, (POS_COMPUTER[0] + 21, POS_COMPUTER[1] + 62)

        self.__clear(lu, rb)
        self.__pv.display_player(player, stakes)

    # from BettingView
    def display_betting(self, money: int):
        self.__clear(POS_BETTING_MENU, (POS_BETTING_MENU[0] + 17, POS_BETTING_MENU[1] + 62))
        self.__bv.display_betting(money)

    # from BettingView
    def display_total_betting(self, money: int):
        self.__clear((POS_TOTAL_MONEY[0], POS_TOTAL_MONEY[1] - 80),
                     (POS_TOTAL_MONEY[0] + NUM_HEIGHT, POS_TOTAL_MONEY[1]))
        self.__bv.display_total_betting(money)

    # from WinnerView
    def display_winner(self, winner: int):
        self.__wv.display_winner(winner)

    # utility method
    def __clear(self, lu: tuple, rb: tuple):
        for i in range(rb[0] - lu[0]):
            with sc.location(lu[0] + i, lu[1]):
                print(" " * (rb[1] - lu[1]))
