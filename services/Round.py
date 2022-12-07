# 한 라운드를 책임지는 클래스입니다.
from ..models.Player import Player
from ..models.Money import Money

class Round:
    def __init__(self) -> None:
        self.winner = Player()
        self.money_earn = Money(0)
        self.players_in = []
        
    def start_round(self, hand_view, players: list) -> None:
        # 라운드가 시작되면 컴퓨터와 플레이어는 자신의 패를 공개하고
        # 가장 높은 밸류를 가진 패가 이깁니다.
        for i in range(len(players)):
            hand_view.show_hand(players[i])
        