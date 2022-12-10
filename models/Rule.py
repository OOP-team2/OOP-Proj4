#섯다 족보 입니다.
class Jokbo:
    # pairs = {
    #     1: (3, 8),
    #     2: (1, 3), #(1,8)
    #     3: (10, 10),
    #     4: (9, 9),
    #     5: (8, 8),
    #     6: (7, 7),
    #     7: (6, 6),
    #     8: (5, 5),
    #     9: (4, 4),
    #     10: (3, 3),
    #     11: (2, 2),
    #     12: (1, 1),
    #     13: (1, 2),  # (2,1)
    #     14: (1, 4),  # (4,1)
    #     15: (9, 1),  # (1,9)
    #     16: (10, 1),  # (1,10)
    #     17: (10, 4),  # (4,10)
    #     18: (4, 6),  # (4,6)
    #     19: (),  # 월 숫자 합 끝자리가 9
    #     20: (),  # 월 숫자 합 끝자리가 8
    #     21: (),  # 월 숫자 합 끝자리가 7
    #     22: (),  # 월 숫자 합 끝자리가 6
    #     23: (),  # 월 숫자 합 끝자리가 5
    #     24: (),  # 월 숫자 합 끝자리가 4
    #     25: (),  # 월 숫자 합 끝자리가 3
    #     26: (),  # 월 숫자 합 끝자리가 2
    #     27: (),  # 월 숫자 합 끝자리가 1
    #     28: (),  # 월 숫자 합 끝자리가 0
    # }

    def __init__(self) -> None:
        # 각 번호를 (1,3) 형식으로 뷰 함수 콜할 때 변환해야함
        self.jokbo_name = {1: '삼팔광땡', 2: '광땡', 3:'장땡', 4:'구땡', 5:'팔땡',
                  6: '칠땡', 7: '육땡', 8:'오땡', 9:'사땡', 10:'삼땡',
                  11: '이땡', 12: '일땡', 13:'알리', 14:'독사', 15:'구삥',
                  16: '장삥', 17: '장사', 18:'세륙', 19:'아홉끗', 20:'여덟끗',
                  21: '일곱끗', 22: '여섯끗', 23: '다섯끗', 24: '사끗', 25: '삼끗',
                  26: '두끗', 27: '한끗', 28: '망통'}
        self.jokbo  = ()

#섯다 족보 입니다.
class Jokbo: 

    def __init__(self) -> None:
        # 각 번호를 (1,3) 형식으로 뷰 함수 콜할 때 변환해야함
        self.jokbo_name = {1: '삼팔광땡', 2: '광땡', 3:'장땡', 4:'구땡', 5:'팔땡',
                  6: '칠땡', 7: '육땡', 8:'오땡', 9:'사땡', 10:'삼땡',
                  11: '이땡', 12: '일땡', 13:'알리', 14:'독사', 15:'구삥',
                  16: '장삥', 17: '장사', 18:'세륙', 19:'아홉끗', 20:'여덟끗',
                  21: '일곱끗', 22: '여섯끗', 23: '다섯끗', 24: '사끗', 25: '삼끗',
                  26: '두끗', 27: '한끗', 28: '망통'}
        self.jokbo  = ()
        
    def create_jokbo()->dict:
        jokbo = dict()
        jokbo['3,8'] = 1
        jokbo['1,3'] = 2
        jokbo['1,8'] = 2                    
        j = 3           
        for i in range(1,11):
            tmp = str(i) + ',' + str(i+10)
            jokbo[tmp] = j
            j+=1
        
        jokbo['1,2,'] = 13
        jokbo['1,4,'] = 14
        jokbo['1,9,'] = 15
        jokbo['1,10,'] = 16
        jokbo['4,10,'] = 17
        jokbo['4,6,'] = 18
        jokbo['9,,'] = 19
        jokbo['8,,'] = 20
        jokbo['7,,'] = 21
        jokbo['6,,'] = 22
        jokbo['5,,'] = 23
        jokbo['4,,'] = 24
        jokbo['3,,'] = 25
        jokbo['2,,'] = 26
        jokbo['1,,'] = 27
        jokbo['0,,'] = 28
        jokbo['4,9,'] = 30
        jokbo['3,7,'] = 31

        return jokbo

    @staticmethod
    def convert_to_pair(pairs, order: int) -> tuple:
        return pairs[order]

    #삼팔광떙 > 광땡 > 땡(1~10) 10개 > 알리(1월과 2월의 조합) > 독사(1월과 4월의 조합) > 구삥 (1월과 9월의 조합)> 장삥(1월과 10월의 조합) 
    # > 장사(4월과 10월의 조합 ) > 세륙(4월과 6월의 조합 )> 갑오(끗수가 9인 것 ) > 끗(두 카드이 합의 끝 수가 1~8인 것 8이 최고) > 망통 (끗수가 0인 것)
    #특수 조합: 
    ##땡잡이: 3월과 7월의 조합으로서 구땡 이하의 족보를 이길(잡을) 수 있습니다.장땡과 광땡,무적의 삼팔 광땡은 잡을 수 없습니다.
    ###만약 상대방 중에 땡이 없다면 끗수가 0이므로 망통으로 계산됩니다.
    ##구사: 4월과 9월의 조합으로서 알리 이하의 족보와(즉, 상대방의 족보 중 가장 높은 것이 알리 이하일 때)이번 판을 물리고 재경기를 할 수 있습니다.
    ##멍텅구리 구사: 열자리 4월과 열자리 9월로 된 조합으로서 9땡 이하의 족보와 (즉, 상대방의 족보 중 가장 높은 것이 9땡 이하 일 때) 재경기를 할 수 있습니다
    ##암행어사:  열자리 4월과 열자리 7로 된 조합으로서 일삼광땡 혹은 일팔광땡을 이길 수 있습니다. 만약 상대방 중에 광땡이 없다면 1끗으로 계산 됩니다.
