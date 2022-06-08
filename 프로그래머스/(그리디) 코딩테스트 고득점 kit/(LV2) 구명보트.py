#LV2 구명보트

from collections import deque

def solution(people, limit):
    
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) == 1:
            answer += 1
            break
            
        if people[0] + people[-1] <= limit:      #40 50 150 160 => 2   (순서대로 하면 안됨)
            people.pop()
            people.popleft()
        else:
            people.pop()         #가장 큰 값 제거 
                        
        answer += 1
    return answer




#2번쨰 풀이
def solution(people, limit):
    people = sorted(people)
    
    left = 0
    right = len(people)-1
    answer = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        answer += 1    
        
    return answer
    
    #투 포인터
    #정렬 후에 => 가장 작은 수, 가장 큰 수 조합   => 무게보다 작으면 둘 다 태우고, 무게보다 크면 큰 수만 태우기

