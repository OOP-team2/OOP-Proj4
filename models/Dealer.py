# 패를 나눠주는 딜러입니다.
from .Hand import Hand
from .Money import Money
from .Player import Player

class Dealer:
    def __init__(self, deck: [Hand], table):
        self.deck: [Hand] = deck
        self.table = table
    def announce_winner(self, player1: Player, player2: Player) -> Player:
        top_value: int = 0
        # 두 플레이어의 패를 비교해서 밸류가 높은 쪽이 승리합니다.
        # 무승부는 존재하지 않습니다.
        return player2
    def distribute_cards(self, player1: Player, player2: Player) -> None:
        # 플레이어에게 카드를 분배합니다.
        # 퍼블릭 메소드를 이용해서 플레이어 내부의 멤버변 수 hands에 새로운 패를 넣어줍니다.
        return

    def check_game_ended(self, players: [Player]) -> bool:
        is_game_ended = False
        looser_count: int = 0
        for i in range(len(players)):
            if players[i].getStakes() == Money(0):
                looser_count += 1
        if looser_count == len(players)-1:
            is_game_ended = True
        return is_game_ended
    
    def start_new_round(self):
        return 0
