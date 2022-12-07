# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
from .Money import Money
from .Hand import Hand
class player(Money,Hand):
       
    def __init__(self)->None:
        Money.__init__(self)
        Hand.__init__(self)
        self.turn:int=0
        self.alive:bool=True
    def setturn(self,turn:int):
        self.turn:int=turn
    def getturn(self):
        return self.turn
    def survive(self): #getalive()
        return self.alive
    
    # def die(self):
    #     self.alive=False
        
    def call(self,otherplayerbet:int):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee
        
    def half(self,otherplayerbet:int,moneyonthegame:int):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee+(self.callfee+moneyonthegame)/2
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee
        
    # def quarter(self,otherplayerbet,moneyonthegame):
    #     self.callfee=abs(self.betsum-otherplayerbet)
    #     self.betfee=self.callfee+(self.callfee+moneyonthegame)/4
    #     if self.betfee>self.money:
    #         self.alive=False
    #     self.betsum+=self.betfee
    #     self.money-=self.betfee
        
    # def ddadang(self,otherplayerbet,otherplayercallfee):
    #     self.callfee=abs(self.betsum-otherplayerbet)
    #     self.betfee=self.callfee+otherplayercallfee
    #     if self.betfee>self.money:
    #         self.alive=False
    #     self.betsum+=self.betfee
    #     self.money-=self.betfee