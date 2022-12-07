# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다. 
from .Player import Player
from .Money import Money
# 컴퓨터 플레이어가 자동으로 폴드, 벳을하게 해야하는데 이 로직을 정해야합니다.
class AutoPlayer(Player):
    def __init__(self, id: int, initial_bet: Money) -> None:
        super().__init__(id, initial_bet)

    def fold(self) -> None:
        pass
