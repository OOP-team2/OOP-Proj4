# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
from .Money import Money
from .Hand import Hand

class Player:     
    def __init__(self,money=Money(500000))->None:
        self.money: Money =money
        self.hands: [Hand] = []
        self.alive:bool=True
        self.callfee:int=0 #콜비용
        self.betsum:int=0 #배팅한 돈의 총액
        self.betfee:int=0 #자신의 턴에 배팅 할 돈
        
    def setturn(self,turn:int)->None:
        self.turn:int=turn
        
    def getturn(self)->int:
        return self.turn
    
    def survive(self)->bool: #getalive()
        return self.alive   #이걸 여기서 처리할까요?
    
    def getbetsum(self)->int:
        return self.betsum
    
    def getbetfee(self)->int:
        return self.betfee
    
    def get_hands(self) -> list:
        return self.hands
    
    def showcallbetfee(self,otherplayerbetsum:int)->int:
        return abs(self.betsum-otherplayerbetsum)
    
    def showhalfbetfee(self,otherplayerbet:int,moneyonthegame:int)->int:
        return abs(self.betsum-otherplayerbet)+(abs(self.betsum-otherplayerbet)+moneyonthegame)//2
    
    def bet(self,money):
        self.money.minus(money)
        self.betsum+=money
    # def die(self):
    #     self.alive=False
        
    def call(self,otherplayerbetsum:int)->None:
        self.callfee=abs(self.betsum-otherplayerbetsum)
        self.betfee=self.callfee
        if self.betfee>self.money.getmoney():
            self.alive=False
        self.betsum+=self.betfee
        self.money.minus(self.betfee)
        
    def half(self,otherplayerbet:int,moneyonthegame:int)->None:
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee+(self.callfee+moneyonthegame)//2
        if self.betfee>self.money.getmoney():
            self.alive=False
        self.betsum+=self.betfee
        self.money.minus(self.betfee)
    
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