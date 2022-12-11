from models.Player import Player
from random import randrange
from models.Action import Action

# This is a Class for a Automatic Player like computer player
class AutoPlayer(Player):
    # constructor for a AutoPlayer
    def __init__(self, initial_stakes: int = 10000) -> None:
        Player.__init__(self, initial_stakes)
        # member variable extended from super class but overrided
        self.player_id = 1

    # member function for taking automatic action randomly
    def auto_action(self) -> Action:
        rannum = randrange(1,4)
        return Action(rannum)