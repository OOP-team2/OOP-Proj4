from models.Player import Player
from models.Jokbo import Jokbo
import random

# This is a Class for a dealer of a game
class Dealer:
    # constructor for a dealer instance
    def __init__(self):
        # member variable for jokbo(table of hand value)
        self.jokbo = Jokbo()

    # member function for announcing a winner
    def announce_winner(self, player1: Player, player2: Player, is_draw: bool) -> Player:
        player1_value = self.calc_rules(player1.hand)
        player2_value = self.calc_rules(player2.hand)
        if not is_draw:
            if player1_value < player2_value:
                return player1
            elif player1_value > player2_value:
                return player2
            elif player1_value == player2_value:
                return Player(-1)
        else:
            if player1_value <= player2_value:
                return player1
            elif player1_value > player2_value:
                return player2

    # member function for distributing cards
    def distribute_cards(self, player1: Player, player2: Player) -> None:
        numbers = [i for i in range(1,21)]
        
        temp_numbers_list = random.sample(numbers, 4)
        
        hand1 = list()
        hand2 = list()
        for i in range(2):
            hand1.append(temp_numbers_list[i])
        for i in range(2,4):
            hand2.append(temp_numbers_list[i])

        player1.set_hand(hand1)
        player2.set_hand(hand2)

    # member function for checking whether game is ended
    def check_game_ended(self, player: Player, computer_player: Player) -> bool:
        is_game_ended = False
        if player.get_stakes() == 0:
            is_game_ended = True
        elif computer_player.get_stakes() == 0:
            is_game_ended = True
        return is_game_ended

    # member function for calculating value of a hand
    def calc_rules(self, paes):
        jokbo = self.jokbo.create_jokbo()
        paes = sorted(paes, key=lambda x: x)
        paes_str = str(paes[0] % 11) + ',' + str(paes[1] % 11)

        return jokbo.get(paes_str) or random.randrange(1,30)