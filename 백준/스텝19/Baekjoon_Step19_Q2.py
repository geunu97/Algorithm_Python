#19단계: 큐, 덱
#2. 카드 앞에서 뒤로 옮기기

from collections import deque

N = int(input())

q = deque([])

for i in range(1,N+1):
    q.append(i)

while True:
    if len(q) == 1:
        break

    q.popleft()

    num = q.popleft()
    q.append(num)

print(q[0])