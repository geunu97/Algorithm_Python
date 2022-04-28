#22단계: 우선순위 큐
#4. 수 하나씩 주어질 때마다 가운데 값 하나씩 출력하기

import heapq
import sys
input = sys.stdin.readline

n = int(input())  #정수의 갯수
# 작은 값과 -중간값-을 저장할 힙과 // 큰 값을 저장할 힙으로 나눈다.
left_heap = []
right_heap = []

for i in range(n):
    num = int(input())
    
    # 돌아가면서 left_heap과 right_heap에 넣어준다. (left_heap 먼저)
    if i % 2 == 1: 
        # 큰 값이 저장된 right힙에서 필요한 값은 최솟값이므로 최소 힙
        heapq.heappush(right_heap, num)
    else:
        # 작은 값이 저장된 left힙에서 필요한 값은 최댓값이므로 최대 힙
        heapq.heappush(left_heap, -num)
    
    # 만약 left힙에 right힙보다 큰 값이 저장되었으면 바꿔준다.
    if right_heap and -left_heap[0] > right_heap[0]:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
        heapq.heappush(left_heap, -heapq.heappop(right_heap))

    # left힙에서 가장 큰 값 출력
    print(-left_heap[0])



#Point
#left_heap 부터 넣고, left_heap, right_heap 번갈아 가면서 넣기
#right_heap에 값이 들어있고, left_heap에 있는 값이 right_heap의 최솟값 보다 크다면 값 바꾸기
