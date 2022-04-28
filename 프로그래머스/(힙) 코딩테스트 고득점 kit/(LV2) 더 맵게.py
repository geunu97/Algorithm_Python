#LV2 더 맵게

import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
        
    answer = 0
    while True:
        if len(heap) == 1:
            if heap[0] >= K:      #예외  ([1,2,3], 11 일 때)
                return answer
            else:
                return -1
        
        first_value = heapq.heappop(heap)
        if first_value >= K:
            return answer
        
        second_value = heapq.heappop(heap)
        result_value = first_value + (second_value*2)
        heapq.heappush(heap,result_value)
        answer += 1


#Point (힙 문제)
#이전에 풀었던 문제와 비슷   (힙에서 2개 빼고, 하나로 합쳐서 다시 넣는 문제)