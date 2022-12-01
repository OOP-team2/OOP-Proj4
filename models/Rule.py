#섯다 족보 입니다.
jokbo_name = {1: '삼팔광땡', 2: '광땡', 3:'장땡', 4:'구땡', 5:'팔땡',
              6: '칠땡', 7: '육땡', 8:'오땡', 9:'사땡', 10:'삼땡',
              11: '이땡', 12: '일땡', 13:'알리', 14:'독사', 15:'구삥',
              16: '장삥', 17: '장사', 18:'세륙', 19:'아홉끗', 20:'여덟끗',
              21: '일곱끗', 22: '여섯끗', 23: '다섯끗', 24: '사끗', 25: '삼끗',
              26: '두끗', 27: '한끗', 28: '망통'}

#삼팔광떙 > 광땡 > 땡(1~10) 10개 > 알리(1월과 2월의 조합) > 독사(1월과 4월의 조합) > 구삥 (1월과 9월의 조합)> 장삥(1월과 10월의 조합) 
# > 장사(4월과 10월의 조합 ) > 세륙(4월과 6월의 조합 )> 갑오(끗수가 9인 것 ) > 끗(두 카드이 합의 끝 수가 1~8인 것 8이 최고) > 망통 (끗수가 0인 것)
#특수 조합: 
##땡잡이: 3월과 7월의 조합으로서 구땡 이하의 족보를 이길(잡을) 수 있습니다.장땡과 광땡,무적의 삼팔 광땡은 잡을 수 없습니다.
###만약 상대방 중에 땡이 없다면 끗수가 0이므로 망통으로 계산됩니다.
##구사: 4월과 9월의 조합으로서 알리 이하의 족보와(즉, 상대방의 족보 중 가장 높은 것이 알리 이하일 때)이번 판을 물리고 재경기를 할 수 있습니다.
##멍텅구리 구사: 열자리 4월과 열자리 9월로 된 조합으로서 9땡 이하의 족보와 (즉, 상대방의 족보 중 가장 높은 것이 9땡 이하 일 때) 재경기를 할 수 있습니다
##암행어사:  열자리 4월과 열자리 7로 된 조합으로서 일삼광땡 혹은 일팔광땡을 이길 수 있습니다. 만약 상대방 중에 광땡이 없다면 1끗으로 계산 됩니다.


jokbo = dict()

jokbo['3,8'] = 1
jokbo['1,3'] = 2
jokbo['1,8'] = 2

j = 3
temp_index = list()
for i in range(1, 11):
    temp_index.append(i)

temp_index = sorted(temp_index, key=lambda x: -x)

for i in temp_index:
    tmp = str(i) + ',' + str(i+10)
    jokbo[tmp] = j
    j+=1

jokbo['1,2,'] = j
j+=1
jokbo['1,4,'] = j
j+=1
jokbo['1,9,'] = j
j+=1
jokbo['1,10,'] = j
j+=1
jokbo['4,10,'] = j
j+=1
jokbo['4,6,'] = j
j+=1
jokbo['9,,'] = j
j+=1
jokbo['8,,'] = j
j+=1
jokbo['7,,'] = j
j+=1
jokbo['6,,'] = j
j+=1
jokbo['5,,'] = j
j+=1
jokbo['4,,'] = j
j+=1
jokbo['3,,'] = j
j+=1
jokbo['2,,'] = j
j+=1
jokbo['1,,'] = j
j+=1
jokbo['0,,'] = j
j+=1
jokbo['4,9,'] = j
j+=1
jokbo['3,7,'] = j

def calc_rules(inp1, jokbo_):
    inp1 = sorted(inp1, key=lambda x:x)
    inp1_str = str(inp1[0]) + ',' + str(inp1[1])

    b = jokbo_.get(inp1_str)

    if b==None:
        tmp_inp1 = inp1[0] % 10
        tmp_inp2 = inp1[1] % 10
        if tmp_inp1 == 0:
            tmp_inp1 +=10
        if tmp_inp2 == 0:
            tmp_inp2 +=10

        #작은걸 앞으로 해준다. 해서 족보 다 일치시키기
        if tmp_inp1 > tmp_inp2:
            temp = tmp_inp1
            tmp_inp1 = tmp_inp2
            tmp_inp2 = temp

        inp1_str = str(tmp_inp1) + ',' + str(tmp_inp2) + ','

        b = jokbo_.get(inp1_str)

        if b==None:
            tmp_inp3 = tmp_inp1 + tmp_inp2
            tmp_inp3 %= 10

            inp3_str = str(tmp_inp3) + ',,'
            b = jokbo_.get(inp3_str)


    return b