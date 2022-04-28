#22단계: 우선순위 큐
#3. 절댓값 힙


import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            a,b = heapq.heappop(heap)
            print(b)

    else:
        heapq.heappush(heap, (abs(x),x))