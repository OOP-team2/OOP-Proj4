#이 파일만 따로 실행시키면 확인 가능합니다
class Hand:
    pass
class Money:
    def __init__(self,money:int =0) -> None:
        self.money=money

    def getmoney(self)->int:
        return self.money    
    
    def setmoney(self,money)->None:
        self.money=money
        
    def plus(self,money:int)->int:
        self.money+=money
        return self.money
    
    def minus(self,money:int)->int: #판에 깔린돈 객체 용
        self.money-=money
        return self.money
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

moneyonthegame=Money(0)
M1=Money(50000)
M2=Money(50000)
p1=Player(M1)
p1.setturn(1)
p1.bet(1000) #맨 처음 천원 씩 걸음
moneyonthegame.plus(1000)
p2=Player(M2)
p2.setturn(2)
p2.bet(1000)
moneyonthegame.plus(1000)

print("-----------------------------")
print("Initial p1")
print(f"p1 money : {p1.money.getmoney()}")
print(f"p1 turn : {p1.getturn()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"p1 betsum : {p1.getbetfee()}")
print(f"p1 callfee : {p1.showcallbetfee(p2.getbetsum())}")
print("-----------------------------")
print("Initial p2")
print(f"p2 money : {p2.money.getmoney()}")
print(f"p2 turn : {p2.getturn()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"p2 betsum : {p2.getbetfee()}")
print(f"p2 callfee : {p2.showcallbetfee(p2.getbetsum())}")
print("-----------------------------")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")

print("-----------------------------")
print("turn 1-1")
print("p1 half")
print(f"p1 callfee : {p1.showcallbetfee(p2.getbetsum())}")
print(f"p1 halffee : {p1.showhalfbetfee(p2.getbetsum(),moneyonthegame.getmoney())}")
p1.half(p2.getbetsum(),moneyonthegame.getmoney())
moneyonthegame.plus(p1.getbetfee())
print(f"p1 money : {p1.money.getmoney()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
print("turn 1-2")
print("p2 half")
print(f"p2 callfee : {p2.showcallbetfee(p1.getbetsum())}")
print(f"p2 halffee : {p2.showhalfbetfee(p1.getbetsum(),moneyonthegame.getmoney())}")
p2.half(p1.getbetsum(),moneyonthegame.getmoney())
moneyonthegame.plus(p2.getbetfee())
print(f"p2 money : {p2.money.getmoney()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
print("turn 2-1")
print("p1 half")
print(f"p1 callfee : {p1.showcallbetfee(p2.getbetsum())}")
print(f"p1 halffee : {p1.showhalfbetfee(p2.getbetsum(),moneyonthegame.getmoney())}")
p1.half(p2.getbetsum(),moneyonthegame.getmoney())
moneyonthegame.plus(p1.getbetfee())
print(f"p1 money : {p1.money.getmoney()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
print("turn 2-2")
print("p2 call")
print(f"p2 callfee : {p2.showcallbetfee(p1.getbetsum())}")
print(f"p2 halffee : {p2.showhalfbetfee(p1.getbetsum(),moneyonthegame.getmoney())}")
p2.call(p1.getbetsum())
moneyonthegame.plus(p2.getbetfee())
print(f"p2 money : {p2.money.getmoney()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
print("turn 3-1")
print("p1 half")
print(f"p1 callfee : {p1.showcallbetfee(p2.getbetsum())}")
print(f"p1 halffee : {p1.showhalfbetfee(p2.getbetsum(),moneyonthegame.getmoney())}")
p1.call(p2.getbetsum())
moneyonthegame.plus(p1.getbetfee())
print(f"p1 money : {p1.money.getmoney()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
print("turn 3-2")
print("p2 call")
print(f"p2 callfee : {p2.showcallbetfee(p1.getbetsum())}")
print(f"p2 halffee : {p1.showhalfbetfee(p1.getbetsum(),moneyonthegame.getmoney())}")
p2.call(p1.getbetsum())
moneyonthegame.plus(p2.getbetfee())
print(f"p2 money : {p2.money.getmoney()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")


        
class Autoplayer(Player):
    pass