#LV2 기능개발

import math

def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        result = 100 - progresses[i]  
        result = math.ceil(result / speeds[i])
        day.append(result)
        
    #print(day)
    
    answer = []
    list_a = [day[0]]
    for i in range(1,len(day)):
        if list_a[0] >= day[i]:          #기준이 리스트 마지막이 아니라 첫번째가 기준
            list_a.append(day[i])
        else:
            answer.append(len(list_a))
            list_a = [day[i]]

    answer.append(len(list_a))      #마지막 처리
    
    return answer