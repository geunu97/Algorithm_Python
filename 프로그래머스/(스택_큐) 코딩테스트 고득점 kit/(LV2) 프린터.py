#LV2 프린터

from collections import deque

def solution(priorities, location):
    list_a = []
    for i in priorities:
        list_a.append([0,i])
    list_a[location][0] = 1
    list_a = deque(list_a)
    
    answer = 1
    while True:
        if len(list_a) == 0:
            return answer
        
        check = 0
        first = list_a[0][1]
        for i in range(1,len(list_a)):
            if first < list_a[i][1]:
                list_a.append(list_a.popleft())
                check = 1
                break    
        
        if check == 0:
            pop_value = list_a.popleft()
            if pop_value[0] == 1:
                return answer
            else:
                answer += 1
    
    

#Point (큐 문제)
#문제 이해 잘못했음
#최댓값이 맨앞에 왔다고 무작정 그대로 return하면 안된다      #(ex)  9 3 5 1 이렇게 이대로 바로 출력하면 안된다)
#최댓값이 맨 앞에 왔을 때 맨 앞값만 빼는 것이고, 나머지는 반복해서 진행된다      (ex) 9뽑고 다시 반복 -> 5뽑고 다시 반복 -> 3뽑고 다시 반복 -> 1뽑기)
#                                                                              #그렇다고 정렬해서 풀면 안됨, 동일한 값 1 1 1일 때 순서가 뒤바뀜


#2번째 풀이
from collections import deque

def solution(priorities, location):
    prior = deque([])
    for i in range(len(priorities)):
        if i == location:
            prior.append([priorities[i],1])
        else:
            prior.append([priorities[i],0])

    answer = []
    while True:
        if len(prior) == 0:
            break
        
        check = 1
        value = prior.popleft()
        for a,b in prior:
            if value[0] < a:
                prior.append(value)
                check = 0
                break
        
        if check == 1:
            answer.append(value)
    
    count = 1
    for a,b in answer:
        if b == 1:
            return count
                          
        count += 1
    
        