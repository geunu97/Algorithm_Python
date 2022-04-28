#19단계: 큐, 덱
#6. 회전하는 큐 

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
list_a = list(map(int,input().split()))

q = deque()
count = 0
for i in range(1, N+1):
    q.append(i)

for i in list_a:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q)//2:
                q.rotate(-1)
                count += 1
            else:
                q.rotate(1)
                count += 1

print(count)


