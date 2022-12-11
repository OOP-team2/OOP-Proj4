from views.WordView import WORD_HEIGHT, WordView
from views.NumberView import NUM_WIDTH
from views.StakeView import StakeView

# Constants
POS_TOTAL_MONEY = (25, 110)
POS_BETTING_MENU = (1, 129)

# View of betting money
class BettingView(WordView):

    def __init__(self):
        # inherit WordView
        super().__init__()
        # own StakeView
        self.sv = StakeView()

    # draw betting money of player
    def display_betting(self, money: int):
        self.display_word("BETTING", POS_BETTING_MENU)
        self.sv.display_stakes((POS_BETTING_MENU[0] + WORD_HEIGHT + 2, POS_BETTING_MENU[1] + 6 * NUM_WIDTH), money)

    # draw total betting money
    def display_total_betting(self, money: int):
        self.sv.display_stakes(POS_TOTAL_MONEY, money)
