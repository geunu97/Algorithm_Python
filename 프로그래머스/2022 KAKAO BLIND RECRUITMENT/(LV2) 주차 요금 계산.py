#LV2 주차 요금 계산

import math

def solution(fees, records):
    dictionary = {}
    
    for i in records:
        i = i.split(' ')  #문자열문제에서 많이 나오는 입력형태, split사용해서 공백으로 구분해주기!!!!!
        
        #한번도 들어온적이 없는 차량
        if i[1] not in dictionary:
            dictionary[i[1]] = [i[0],i[2],0]      #시간, IN/OUT, 누적시간
            continue
        
        #들어와 있어서 다시 OUT하는 차량
        if dictionary[i[1]][1] == 'IN' and i[2] == 'OUT':
            hour = int(i[0][:2]) - int(dictionary[i[1]][0][:2])
            minute = int(i[0][3:5]) - int(dictionary[i[1]][0][3:5])
            time = hour * 60 + minute      #분 단위, 뺀 시간
            
            dictionary[i[1]] = [0, 'OUT', dictionary[i[1]][2] + time]   #시간, IN/OUT, 누적시간
            
        #나갔었는데 다시 IN하는 차량
        elif dictionary[i[1]][1] == 'OUT' and i[2] == 'IN':
            dictionary[i[1]] = [i[0],'IN',dictionary[i[1]][2]]  #시간, IN/OUT, 누적시간      
    
    
    #마무리) 들어온 차량중에서 23:59분에 모두 내보내기
    for key in dictionary:
        if dictionary[key][1] == 'IN':
            hour = 23 - int(dictionary[key][0][:2])
            minute = 59 - int(dictionary[key][0][3:5])
            time = hour * 60 + minute      #분 단위, 뺀 시간  
            
            dictionary[key] = [0, 'OUT', dictionary[key][2] + time]   #시간, IN/OUT, 누적시간
    
    #print(dictionary)
    #요금정산
    answer = []
    for key in dictionary:
        if dictionary[key][2] <= fees[0]:    #기본시간 이하라면 기본요금만
            answer_fee = fees[1]
        else:
            answer_fee = fees[1] + math.ceil((dictionary[key][2]-fees[0]) / fees[2]) * fees[3] 
        
        answer.append([key, answer_fee])
    

    #차량번호 낮은 순으로 정렬
    answer = sorted(answer, key = lambda x: x[0])
    
    result = []
    for a,b in answer:
        result.append(b)
        
    return result


#Point
#딕셔너리로 풀었음, 결코 쉽지는 않고 생각보다 까다로웠음