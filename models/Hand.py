# 화투 패 하나를 책임지는 클래스입니다.
class Hand:
    def __init__(self, hold = None):

        # 입력하지 않은 경우(필요없는 경우 제거 요망)
        if hold == None :
            self.hold = " "
        #맴버변수 초기화
        self.hold = hold

    def get_value(self):
        return self.hold


