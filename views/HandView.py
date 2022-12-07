import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from services.TxtReader import TxtReader
from console import sc

POS_PLAYER = [(32, 66), (32, 96)]
POS_COMPUTER = [(0, 66), (0, 96)]
CARD_HEIGHT = 23


class HandView:

    def __init__(self) -> None:
        self.hands = TxtReader().read_hands()

    def display_hand(self, player: int, hand: dict = (0, 0), front: bool = True):
        if player == 0:
            pos = POS_PLAYER
        else:
            pos = POS_COMPUTER

        for i in range(CARD_HEIGHT):
            if front:
                with sc.location(pos[0][0]+i, pos[0][1]):
                    print(self.hands[str(hand[0])][i], end="")

                with sc.location(pos[1][0]+i, pos[1][1]):
                    print(self.hands[str(hand[1])][i], end="")

            else:
                with sc.location(pos[0][0]+i, pos[0][1]):
                    print(self.hands["0"][i], end="")

                with sc.location(pos[1][0]+i, pos[1][1]):
                    print(self.hands["0"][i], end="")
