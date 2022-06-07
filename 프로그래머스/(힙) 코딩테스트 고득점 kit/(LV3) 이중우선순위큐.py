#LV3  이중우선순위큐

from collections import deque

def solution(operations):              
    list_a = []
    
    for i in operations:
        i = i.split(' ') 
        if i[0] == 'I':
            list_a.append(int(i[1]))
            list_a = sorted(list_a)
            list_a = deque(list_a)    
        
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


#2번째 풀이
from collections import deque

def solution(operations):
    q = deque([])
    
    for i in operations:
        i = i.split(' ')

        if i[0] == 'I':
            q.append(int(i[1]))
            q = deque(sorted(q))          #큐에서 정렬하면 큐 풀려서, 단순리스트 됨
        
        elif i[1] == '1' and len(q) > 0:
            q.pop()

        elif i[1] == '-1' and len(q) > 0:
            q.popleft()
    
    if len(q) == 0:
        return [0,0]
    else:
        return [q[-1],q[0]]


#1. 하나의 큐로 값을 넣을 때마다 정렬, 큐로 변환해준다
#2. 최댓값을 뺄 때는 가장 오른쪽, 최솟값을 뺄 때는 가장 왼쪽에서 빼주면 된다