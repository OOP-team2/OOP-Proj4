class hand:
    pass
class money:
    
    def __init__(self,money=0):
        self.money=money
        self.betsum=0
        self.callfee=10000
        self.betfee=0
        
    def getmoney(self):
        return self.money
    
    def getbetsum(self):
        return self.betsum
    
    def getcallfee(self):
        return self.callfee
    
    def getbetfee(self):
        return self.betfee
    
    def setmoney(self,money):
        self.money=money
    
    def bet(self,bet):
        self.money-=bet
        
    def playerbet(self,playerbet): #판에 깔린돈 객체 용
        self.money+=playerbet


    
class player(money,hand):
       
    def __init__(self):
        money.__init__(self)
        hand.__init__(self)
        self.turn=0
        self.alive=True
    def setturn(self,turn):
        self.turn=turn
    def getturn(self):
        return self.turn
    def survive(self): #getalive()
        return self.alive
    
    def die(self):
        self.alive=False
        
    def call(self,otherplayerbet):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee
        
    def half(self,otherplayerbet,moneyonthegame):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee+(self.callfee+moneyonthegame)/2
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee
        
    def quarter(self,otherplayerbet,moneyonthegame):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee+(self.callfee+moneyonthegame)/4
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee
        
    def ddadang(self,otherplayerbet,otherplayercallfee):
        self.callfee=abs(self.betsum-otherplayerbet)
        self.betfee=self.callfee+otherplayercallfee
        if self.betfee>self.money:
            self.alive=False
        self.betsum+=self.betfee
        self.money-=self.betfee

p1=player()
p1.setturn(0)
p1.setmoney(10000000)
p1.bet(10000)
print("-----------------------------")
print("set p1")
print(f"p1 money : {p1.getmoney()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"p1 callfee : {p1.getcallfee()}")

print("-----------------------------")
p2=player()
p2.setturn(2)
p2.setmoney(10000000)
p2.bet(10000)
print("set p2")
print(f"p2 money : {p1.getmoney()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"p2 callfee : {p2.getcallfee()}")
print("-----------------------------")




moneyonthegame=money()
moneyonthegame.setmoney(p1.getcallfee()+p2.getcallfee())
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")

p1.half(p2.getbetsum(),moneyonthegame.getmoney())
moneyonthegame.playerbet(p1.getbetfee())
print("-----------------------------")
print("p1 half")
print(f"p1 money : {p1.getmoney()}")
print(f"p1 betsum : {p1.getbetsum()}")
print(f"p1 callfee : {p1.getcallfee()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")
p2.quarter(p1.getbetsum(),moneyonthegame.getmoney())
moneyonthegame.playerbet(p2.getbetfee())
print("p2 quarter")
print(f"p2 money : {p2.getmoney()}")
print(f"p2 betsum : {p2.getbetsum()}")
print(f"p2 callfee : {p2.getcallfee()}")
print(f"moneyonthegame : {moneyonthegame.getmoney()}")
print("-----------------------------")



        
class Autoplayer(player):
    pass