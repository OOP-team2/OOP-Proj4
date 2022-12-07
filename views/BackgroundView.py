from console.screen import sc
from HandView import HandView
from WordView import *
from NumberView import *
from PlayerView import PlayerView
from BettingView import BettingView

ROW_WINDOW = 192
COL_WINDOW = 56

BORDER_WIDTH = 63
PLAYER_BORDER_HEIGHT = 23
MENU_BORDER_HEIGHT = 35

POS_PLAYER_BORDER_RIGHT = 63
POS_MENU_BORDER_LEFT = 128
POS_MENU = (COL_WINDOW - 35, 130)


class Background(NumberView, WordView):
    def __init__(self):
        NumberView.__init__(self)
        WordView.__init__(self)
        os.system(f"mode {ROW_WINDOW},{COL_WINDOW}")
        os.system("color 0f")
        os.system("cls")

        self.__draw_player_box()
        self.__draw_menu_box()

    def __draw_player_box(self):
        for i in range(PLAYER_BORDER_HEIGHT):
            with sc.location(i-1, POS_PLAYER_BORDER_RIGHT):
                print("|")

            with sc.location(COL_WINDOW - (i+1), POS_PLAYER_BORDER_RIGHT):
                print("|")

        for i in range(BORDER_WIDTH):
            with sc.location(PLAYER_BORDER_HEIGHT - 1, i):
                print("-")

            with sc.location(COL_WINDOW - (PLAYER_BORDER_HEIGHT + 1), i):
                print("_")

    def __draw_menu_box(self):
        for i in range(MENU_BORDER_HEIGHT):
            with sc.location(COL_WINDOW - (i + 2), POS_MENU_BORDER_LEFT):
                print("|")

        for i in range(BORDER_WIDTH):
            with sc.location(COL_WINDOW - (MENU_BORDER_HEIGHT + 1), POS_MENU_BORDER_LEFT + i):
                print("-")

        for i, word in enumerate(["EXIT", "CALL", "HALF", "DIE"]):
            self.display_number(i, (POS_MENU[0] + (i * (NUM_HEIGHT+2)), POS_MENU[1]))
            self.display_word(word, (POS_MENU[0] + (i * (NUM_HEIGHT+2)), POS_MENU[1] + (2 * NUM_WIDTH)))

    def display_input(self, pos: tuple = (COL_WINDOW - (MENU_BORDER_HEIGHT + 2), POS_MENU_BORDER_LEFT)) -> int:
        with sc.location(pos[0], pos[1]):
            choice = input("CHOICE : ")
        return choice


# sample code
screen = Background()
hv = HandView()
pv = PlayerView()
bv = BettingView()

hv.display_hand(0, (3, 7))
hv.display_hand(1, front=False)
pv.display_player(0, 100000)
pv.display_player(1)
bv.display_betting(10000)
bv.display_total_betting(0)

screen.display_input()
