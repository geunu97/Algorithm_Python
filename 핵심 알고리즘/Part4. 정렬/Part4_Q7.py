#Part4. 정렬
#문제 7. 카드 정렬하기 (백준 1715)

import heapq

N = int(input())
list_a = []
for i in range(N):
    list_a.append(int(input()))

heap = []
for i in list_a:
    heapq.heappush(heap,i)

result = 0
while len(heap) != 1:   #원소가 1개 남을 때까지
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one+two
    result += sum_value
    heapq.heappush(heap,sum_value)

print(result)

#Point
#우선 순위 큐로 풀기(최소힙)
#가장 작은거 2개 빼서 결과에 더해주고 덧셈한거 다시 힙에 넣기 (1개 남을때까지 반복)
