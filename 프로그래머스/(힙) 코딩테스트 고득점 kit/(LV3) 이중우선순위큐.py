#LV3  이중우선순위큐

from collections import deque

def solution(operations):              
    list_a = []
    
    for i in operations:
        i = i.split(' ') 
        if i[0] == 'I':
            list_a.append(int(i[1]))
            list_a = sorted(list_a)
            list_a = deque(list_a)    #덱을 정렬하면 리스트로 변환되기 때문
        
        elif i[1] == '1':
            if len(list_a) == 0:
                continue
            else:
                list_a.pop()
        
        elif i[1] == '-1':
            if len(list_a) == 0:
                continue
            else:
                list_a.popleft()     
    
    
    if len(list_a) == 0:
        return [0,0]
    else:
        return [list_a[-1],list_a[0]]


#Point
#힙으로 풀지 말고, 큐로 푸는 문제
#넣을 때는 넣고 정렬해주기
#뺄 때는 최소값 가장 왼쪽에서, 최댓값 가장 오른쪽에서 빼주면 됨