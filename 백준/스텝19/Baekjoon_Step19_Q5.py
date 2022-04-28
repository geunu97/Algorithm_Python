#19단계: 큐, 덱
#5. 8가지 명령어

from collections import deque

import sys
input = sys.stdin.readline

N = int(input())

q = deque([])
for _ in range(N):
    list_a = list(input().split())
    
    if len(list_a) == 2:
        if list_a[0] == 'push_front':
            q.appendleft(int(list_a[1]))
        if list_a[0] == 'push_back':
            q.append(int(list_a[1]))
    else:
        if list_a[0] == 'front':
            if len(q) == 0:
                print('-1')
            else:
                print(q[0])
        
        if list_a[0] == 'back':
            if len(q) == 0:
                print('-1')
            else:
                print(q[-1])

        elif list_a[0] == 'size':
            print(len(q))

        elif list_a[0] == 'empty':
            if len(q) == 0:
                print('1')
            else:
                print('0')

        elif list_a[0] == 'pop_front':
            if len(q) == 0:
                print('-1')
            else:
                print(q.popleft())
        elif list_a[0] == 'pop_back':
            if len(q) == 0:
                print('-1')
            else:
                print(q.pop())