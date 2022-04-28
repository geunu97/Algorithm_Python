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


#Point
#순서대로 2쌍 잡지말고, 맨처음 맨끝으로 2쌍 잡았어야 됨 

