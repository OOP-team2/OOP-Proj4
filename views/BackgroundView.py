from console.screen import sc
from views.WordView import *
from views.NumberView import *

WIDTH_WINDOW = 192
HEIGHT_WINDOW = 56

BORDER_WIDTH = 63
PLAYER_BORDER_HEIGHT = 23
MENU_BORDER_HEIGHT = 35

POS_PLAYER_BORDER_RIGHT = 63
POS_MENU_BORDER_LEFT = 128
POS_MENU = (HEIGHT_WINDOW - 35, 130)
POS_ROUNDS = (25, 1)

MENU = {
    "EXIT": 0,
    "DIE": 1,
    "CALL": 2,
    "HALF": 3
}


class BackgroundView(NumberView, WordView):
    def __init__(self):
        NumberView.__init__(self)
        WordView.__init__(self)
        os.system(f"mode {WIDTH_WINDOW + 1},{HEIGHT_WINDOW + 1}")
        os.system("color 0f")
        os.system("cls")

    def display_background(self):
        self.__draw_player_box()
        self.__draw_menu_box()

    def display_menu(self, actions: [str] = ("EXIT", "DIE", "CALL", "HALF")):
        # for i in range(MENU_BORDER_HEIGHT - 1):
        #     with sc.location(POS_MENU[0] + i, POS_MENU[1]):
        #         print(" " * 64)

        for i, word in enumerate(actions):
            self.display_number(MENU[word], (POS_MENU[0] + (i * (NUM_HEIGHT+2)), POS_MENU[1]))
            self.display_word(word, (POS_MENU[0] + (i * (NUM_HEIGHT+2)), POS_MENU[1] + (2 * NUM_WIDTH)))

    def display_rounds(self, rounds: int = 1):
        rounds_str = str(rounds)
        self.display_word("R", POS_ROUNDS)
        for i, num in enumerate(rounds_str):
            self.display_number(num, (POS_ROUNDS[0], POS_ROUNDS[1] + (i + 1) * NUM_WIDTH))

    def display_input(self) -> int:
        pos = (HEIGHT_WINDOW - (MENU_BORDER_HEIGHT + 2), POS_MENU_BORDER_LEFT)
        while True:
            with sc.location(pos[0], pos[1]):
                choice = input("CHOICE : ")
                if "0" <= choice <= "3":
                    return int(choice)
                else:
                    with sc.location(pos[0], pos[1]):
                        print(" " * 50)

    def __draw_player_box(self):
        for i in range(PLAYER_BORDER_HEIGHT):
            with sc.location(i-1, POS_PLAYER_BORDER_RIGHT):
                print("|")

            with sc.location(HEIGHT_WINDOW - (i + 1), POS_PLAYER_BORDER_RIGHT):
                print("|")

        for i in range(BORDER_WIDTH):
            with sc.location(PLAYER_BORDER_HEIGHT - 1, i):
                print("-")

            with sc.location(HEIGHT_WINDOW - (PLAYER_BORDER_HEIGHT + 1), i):
                print("_")

    def __draw_menu_box(self):
        for i in range(MENU_BORDER_HEIGHT):
            with sc.location(HEIGHT_WINDOW - (i + 2), POS_MENU_BORDER_LEFT):
                print("|")

        for i in range(BORDER_WIDTH):
            with sc.location(HEIGHT_WINDOW - (MENU_BORDER_HEIGHT + 1), POS_MENU_BORDER_LEFT + i):
                print("-")
