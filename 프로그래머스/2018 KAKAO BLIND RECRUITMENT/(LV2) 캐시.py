#LV2 캐시

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:        #예외처리
        return len(cities) * 5
    
    db_list = deque([]) 
    answer = 0
    
    for i in cities:
        i = i.upper()    #대소문자 구별X
        
        if len(db_list) < cacheSize:  #길이가 아직 안채워졌으면
            if i in db_list:
                answer += 1
                db_list = list(db_list)
                db_list.pop(db_list.index(i))    #큐일때 특정인덱스로 pop()사용 불가, 리스트로 바꿔야댐
                db_list = deque(db_list)
            else:
                answer += 5
                
            db_list.append(i)
            
        elif len(db_list) == cacheSize:   #길이가 딱 채워졌으면
            if i in db_list:
                answer += 1
                db_list = list(db_list)
                db_list.pop(db_list.index(i))
                db_list = deque(db_list)
            else:
                answer += 5
                db_list.popleft()
                
            db_list.append(i)

    return answer


#Point
#캐시 교체 알고리즘 Least Recently Used: (가장 가장 최근에 사용되지 않은 것) -> db_list에 문자가 있다면 그 문자를 빼고 마지막 위치에 넣어야한다 (예외)
 
 