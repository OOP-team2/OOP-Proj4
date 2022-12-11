# 패를 나눠주는 딜러입니다.
from models.Hand import Hand
from models.Player import Player
import itertools
import random
from models.Jokbo import Jokbo

class Dealer:
    def __init__(self):
        self.jokbo = Jokbo()

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

    def distribute_cards(self, player1: Player, player2: Player) -> None:
        
        # 플레이어에게 카드를 분배합니다.
        # 퍼블릭 메소드를 이용해서 플레이어 내부의 멤버변 수 hands에 새로운 패를 넣어줍니다.
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

    def check_game_ended(self, player: Player, computer_player: Player) -> bool:
        is_game_ended = False
        if player.get_stakes() == 0:
            is_game_ended = True
        elif computer_player.get_stakes() == 0:
            is_game_ended = True
        return is_game_ended

    def calc_rules(self, paes):
        jokbo = self.jokbo.create_jokbo()
        paes = sorted(paes, key=lambda x: x)
        paes_str = str(paes[0] % 11) + ',' + str(paes[1] % 11)

        return jokbo.get(paes_str) or random.randrange(1,30)