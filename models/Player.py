# 게임을 하는 플레이어입니다.
# 컴퓨터 플레이어 클래스는 플레이어 클래스로부터 파생됩니다.
class player(Money,Hand):
       
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