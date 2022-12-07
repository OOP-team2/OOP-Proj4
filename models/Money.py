class Money:
    def __init__(self,money:int =0) -> None:
        self.money=money
        self.betsum=0
        self.callfee=10000
        self.betfee=0
        
    def getmoney(self)->int:
        return self.money
    
    def getbetsum(self)->int:
        return self.betsum
    
    def getcallfee(self)->int:
        return self.callfee
    
    def getbetfee(self)->int:
        return self.betfee
    
    # def setmoney(self,money:int=0)->None:
    #     self.money=money
    
    def bet(self,bet:int)->None:
        self.money-=bet
        
    def playerbet(self,playerbet:int)->None: #판에 깔린돈 객체 용
        self.money+=playerbet
