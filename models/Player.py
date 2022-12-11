from models.Action import Action

# This is a Class for a player of the game
class Player:
    # constructor for a player instance
    def __init__(self, initial_stakes: int = 10000) -> None:
        # member variable for the stakes
        self.stakes: int = initial_stakes
        # member variable for the hand a player has
        self.hand = []
        # member variable for player id
        self.player_id: int = 0
        # member variable for available actions of a player
        self.available_actions = [action for action in Action]
        # member variable for available actions when a player did call
        self.actions_did_call = [Action(0), Action(1), Action(2)]
        # member variable for available actions when a player is first turn
        self.actions_on_first_turn = [Action(0), Action(1), Action(3)]

    # member function for getting a player id
    def get_id(self) -> int:
        return self.player_id
    
    # member function for getting a player stakes
    def get_stakes(self):
        return self.stakes

    # member function for betting certain amount of money
    def bet(self, money: int) -> None:
        self.stakes -= money
    
    # member function for taking winning money
    def take(self, money: int) -> None:
        self.stakes += money
    
    # member function for returning available actions
    def actions(self, round_turn: int, first_turn: int = 0, did_call: bool = False):
        if first_turn == self.player_id and round_turn == 1:
            return self.actions_on_first_turn
        elif did_call:
            return self.actions_did_call
        else:
            return self.available_actions

    # member function for setting a hand of a player
    def set_hand(self, hand) -> None:
        self.hand.clear()
        self.hand.extend(hand)

    # member function for getting a hand of a player
    def get_hand(self) -> list:
        return self.hand
