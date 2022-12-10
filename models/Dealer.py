# 패를 나눠주는 딜러입니다.
from .Hand import Hand
from .Player import Player
from .Hand import Hand
import itertools
import random
import Rule

class Dealer:
    def __init__(self):
        pass
    def announce_winner(self, player1: Player, player2: Player) -> Player:
        player1_value = Rule.calc_rules(player1.hands[0],Rule.jokbo)
        player2_value = Rule.calc_rules(player2.hands[0],Rule.jokbo)

        if player1_value < player2_value:
            return player1
        elif player1_value > player2_value:
            return player2
        elif player1_value == plaeyr2_value:
            print("무승부 입니다")
            Round.start_round()

        # 두 플레이어의 패를 비교해서 밸류가 높은 쪽이 승리합니다.
        # 무승부는 존재하지 않습니다.
    def distribute_cards(self, player1: Player, player2: Player) -> None:
        # 플레이어에게 카드를 분배합니다.
        # 퍼블릭 메소드를 이용해서 플레이어 내부의 멤버변 수 hands에 새로운 패를 넣어줍니다.
        temp_player_pae = list()

        temp = list(itertools.combinations(range(1, 21), 2))
        temp_card_combination = random.sample(sorted(temp), 2)

        player1.set_hand(list(map(int, temp_card_combination[0])))
        player2.set_hand(list(map(int, temp_card_combination[1])))

    def check_game_ended(self, player: Player, computer_player: Player) -> bool:
        is_game_ended = False
        if player.getStakes() == 0:
            is_game_ended = True
        elif computer_player.getStakes() == 0:
            is_game_ended = True
        return is_game_ended

    def calc_rules(self, paes):
        jokbo = Rule.Jokbo.create_jokbo()
        paes = sorted(paes, key=lambda x: x)
        paes_str = str(paes[0]) + ',' + str(paes[1])

        b = jokbo.get(paes_str)

        if b == None:
            tmp_paes = paes[0] % 10
            tmp_paes = paes[1] % 10
            if tmp_paes == 0:
                tmp_paes += 10
            if tmp_paes == 0:
                tmp_paes += 10

            # 작은걸 앞으로 해준다. 해서 족보 다 일치시키기
            if tmp_paes > tmp_paes:
                temp = tmp_paes
                tmp_paes = tmp_paes
                tmp_paes = temp

            paes_str = str(tmp_paes) + ',' + str(tmp_paes) + ','

            jokbo_power = jokbo.get(paes_str)

            if jokbo_power == None:
                tmp_inp3 = tmp_paes + tmp_paes
                tmp_inp3 %= 10

                inp3_str = str(tmp_inp3) + ',,'
                jokbo_power = jokbo.get(inp3_str)

        return jokbo_power
