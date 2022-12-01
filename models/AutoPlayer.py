# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다.
from Player import Player
class AutoPlayer(Player):
    def __init__(self) -> None:
        super().__init__()