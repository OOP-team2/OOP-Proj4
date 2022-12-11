#섯다 족보 입니다.
class Jokbo: 
    def __init__(self) -> None:
        self.jokbo_name = {1: '삼팔광땡', 2: '광땡', 3:'장땡', 4:'구땡', 5:'팔땡',
                  6: '칠땡', 7: '육땡', 8:'오땡', 9:'사땡', 10:'삼땡',
                  11: '이땡', 12: '일땡', 13:'알리', 14:'독사', 15:'구삥',
                  16: '장삥', 17: '장사', 18:'세륙', 19:'아홉끗', 20:'여덟끗',
                  21: '일곱끗', 22: '여섯끗', 23: '다섯끗', 24: '사끗', 25: '삼끗',
                  26: '두끗', 27: '한끗', 28: '망통'}
        self.jokbo  = ()
    
    def create_jokbo(self)->dict:
        jokbo = dict()
        jokbo['3,8'] = 1
        jokbo['1,3'] = 2
        jokbo['1,8'] = 2 

        jokbo['10,10'] = 3
        jokbo['9,9'] = 4
        jokbo['8,8'] = 5
        jokbo['7,7'] = 6
        jokbo['6,6'] = 7
        jokbo['5,5'] = 8
        jokbo['4,4'] = 9
        jokbo['3,3'] = 10
        jokbo['2,2'] = 11
        jokbo['1,1'] = 12

        jokbo['1,2'] = 13
        jokbo['1,4'] = 14 
        jokbo['1,9'] = 15 
        jokbo['1,10'] = 16 
        jokbo['4,10'] = 17 
        jokbo['4,6'] = 18

        #g5
        jokbo['2,7'] = 19 
        jokbo['3,6'] = 20
        jokbo['4,5'] = 21
        jokbo['9,10'] = 22

        # 1ggt
        jokbo['2,9'] = 30
        jokbo['4,7'] = 30
        jokbo['5,6'] = 30

        jokbo['2,10'] = 29
        jokbo['3,9'] = 29
        jokbo['4,8'] = 29
        jokbo['5,7'] = 29

        jokbo['3,10'] = 28
        jokbo['4,9'] = 28
        jokbo['5,8'] = 28
        jokbo['6,7'] = 28
 
        jokbo['5,9'] = 27
        jokbo['6,8'] = 27

        jokbo['5,10'] = 26
        jokbo['6,10'] = 25
        jokbo['7,10'] = 24
        jokbo['8,10'] = 23

        # mt
        jokbo['1,9'] = 30
        jokbo['2,8'] = 30
        jokbo['3,7'] = 30


        return jokbo