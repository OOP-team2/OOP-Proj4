# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.

from models.Action import Action

class Player:
    def __init__(self, initial_stakes: int = 10000) -> None:
        self.stakes: int = initial_stakes
        self.hand = []
        self.player_id: int = 0
        self.available_actions = [action for action in Action]
        self.actions_did_call = [Action(0), Action(1), Action(2)]
        self.actions_on_first_turn = [Action(0), Action(1), Action(3)]

    def get_id(self) -> int:
        return self.player_id
    def get_stakes(self):
        return self.stakes
    def bet(self, money: int) -> None:
        self.stakes -= money
    def take(self, money: int) -> None:
        self.stakes += money
    def actions(self, round_turn: int, first_turn: int = 0, did_call: bool = False) -> [Action]:
        # 단 첫턴인 경우에는 콜 못합니다.
        # 한번 콜하면 콜 다이 밖에 못함
        if first_turn == self.player_id and round_turn == 1:
            return self.actions_on_first_turn
        elif did_call:
            return self.actions_did_call
        else:
            return self.available_actions

    def set_hand(self, hand: [int]) -> None:
        self.hand.clear()
        self.hand.extend(hand)

    def get_hand(self) -> list:
        return self.hand
