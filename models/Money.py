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