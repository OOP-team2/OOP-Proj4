# 컴퓨터 플레이어입니다. 플레이어로부터 파생됩니다. 
from models.Player import Player
from random import randrange
from models.Action import Action

# 컴퓨터 플레이어가 자동으로 폴드, 벳을하게 해야하는데 이 로직을 정해야합니다.
class AutoPlayer(Player):
    def __init__(self, initial_stakes: int = 10000) -> None:
        Player.__init__(self, initial_stakes)
        self.player_id = 1

    def auto_action(self) -> Action:
        rannum = randrange(1,4)
        # random choose one action
        return Action(rannum)