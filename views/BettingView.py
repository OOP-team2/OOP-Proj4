from WordView import WORD_HEIGHT, WordView
from NumberView import NUM_WIDTH
from StakeView import StakeView

POS_TOTAL_MONEY = (25, 110)
POS_BETTING_MENU = (1, 129)

class BettingView(WordView):

    def __init__(self):
        super().__init__()
        self.sv = StakeView()

    def display_betting(self, money: int):
        self.display_word("BETTING", POS_BETTING_MENU)
        self.sv.display_stakes((POS_BETTING_MENU[0] + WORD_HEIGHT + 2, POS_BETTING_MENU[1] + 6 * NUM_WIDTH), money)

    def display_total_betting(self, money: int):
        self.sv.display_stakes(POS_TOTAL_MONEY, money)
