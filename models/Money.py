# 베팅 금액을 책임지는 클래스입니다.
class Money:
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