#LV3 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    now = 0
    l = len(jobs)
    jobs.sort(key=lambda x:(x[0], x[1]))
    heap = []

    while jobs or heap:
        while jobs:
            if jobs[0][0] <= now:
                x = jobs.pop(0)
                heapq.heappush(heap, [x[1], x[0]])
            else:
                break
                
        if heap:
            taken_time, request_time = heapq.heappop(heap)
            now += taken_time
            answer += (now-request_time)
        else:
            now += 1

    return answer//l

'''
1. 하드디스크가 작업을 수행하고있지 않을 때는 먼저 들어온 요청부터 처리한다.   (정렬)
2. 대기목록 만들기 (새로운 배열 heap 생성)
3. 소요시간이 최소가 되기 위해서는 대기목록에 있는 작업들 중 작업 시간이 가장 작은 것부터 처리한다. (작업시간에 대해 최소 구하기 ([작업시간, 요청시간]))
4. 작업이 중간에 끊겨있을 수 있다. (테스트케이스19번)  → 이때는 현재 시간(now)를 1초씩 증가시키며 요청을 받고 이를 요청이 들어올 때까지 반복한다.

꼭 다시 보고 제대로 이해하기!
출처 https://blog.naver.com/deluv98/222620559116
'''