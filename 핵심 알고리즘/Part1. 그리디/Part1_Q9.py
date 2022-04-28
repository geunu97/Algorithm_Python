#Part1. 그리디
#문제 9. 2019 카카오 LV4 무지의 먹방 라이브 (프로그래머스)
# [3,1,2] 가 있을 때 n초 후에 나타내는 자리는? 1초당 한번씩 옆으로 이동하며, 0초일 때는 pass 

import heapq

def solution(food_times,k):
    if sum(food_times) <= k:    #나중에 모두 0이 되는데 k가 남아있는데 갈 곳이 없을 때
        return -1

    #최소 힙 생성
    q = []
    #최소 힙에 모든 값 넣기  [food_times[i],i+1] 리스트 형태로            =>  [3,1] , [1,2] , [2,1] 이렇게 넣는다면
    #                        [시간 초 , 해당인덱스+1]                     =>  [1, 2], [3, 1], [2, 3] 맨 앞에 기준으로 됨
    for i in range(len(food_times)):
        heapq.heappush(q,[food_times[i],i+1])

    sum_value = 0  #총 계산횟수
    previous = 0   #1바퀴 돌때마다 모두 -1씩 빼줘야 되니깐!
    length = len(food_times)

    #최소값 구한 후 그 값이 0이 될 때까지 몇바퀴 돌아야되는지만 구하는 것  
    #q[0][0] - previous는 다음 최솟값에도 이전 최솟값만큼 1바퀴당 -1씩 해줘야되니깐
    while sum_value + (( q[0][0] - previous ) * length) <= k:   #몇바퀴 도는지만 구하기 위해 (나머지만 있을 때는 사용 안하는 조건)
        now = heapq.heappop(q)[0]     #최소값 지우기(루트 노트)   // # now는 최솟값 나타냄
        sum_value += (now - previous) * length   #1바퀴당 몇번 계산하는지 구함
        length -= 1   #최솟값 지웠으니깐 길이도 1빼기
        previous = now   #previous는 최솟값 나타냄 

    #나머지만 남았을 때 시작
    #원래 순서대로 맞추기 위해 정렬
    result = sorted(q,key = lambda x: x[1])
    #나머지 값 구하기
    return result[(k - sum_value) % length][1]

food_times = [3, 1, 2]
print(solution(food_times,5))

#쉽게 최솟값 이용하고 쉽게 최솟값 데이터 없애기 위해 최소 힙 사용!!!!



