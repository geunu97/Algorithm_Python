#LV2 캐시
 

#2번째 풀이
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:    #예외
        return 5 * len(cities)
    
    cache = deque([])
    answer = 0
    for i in cities:
        i = i.upper()  #대소문자 구별X
        
        if len(cache) < cacheSize:
            if i in cache:
                answer += 1
                cache = list(cache)
                cache.pop(cache.index(i))  #큐일때 특정인덱스 제거 불가,  pop()사용 불가, 리스트로 바꿔야댐
                cache = deque(cache)
            else:
                answer += 5
            cache.append(i)
         
        else:
            if i in cache:
                answer += 1
                cache = list(cache)
                cache.pop(cache.index(i))
                cache.append(i)
                cache = deque(cache)
                
            else:
                answer += 5
                cache.popleft()
                cache.append(i)
        
    return answer


#고정 크기의 캐시에 해당 문자열이 있는지 검사, 있으면 +1, 없으면 +5 걸리는 문제

'''
1. 고정 크기의 캐시에 특정 값이 있는지 없는지 검사합니다
   1-1. 캐시에 특정 값이 없다면, 들어온 순서대로 pop과 append를 해줍니다 (큐, answer+5)
   1-2. [핵심] 캐시에 특정 값이 있다면, 특정 값이 있던 인덱스 자리를 제거해주고 큐의 마지막 인덱스 자리로 교체해줍니다 (LRU, answer +1)
'''