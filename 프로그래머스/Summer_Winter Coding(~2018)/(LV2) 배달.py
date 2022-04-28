#LV2 배달
#한 정점에서 모든 정점까지의 거리 중에서 K시간 이내로 도착할 수 있는 정점 찾기

import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
    
    INF = 987654321
    distance = [INF] * (N+1)
    
    q=[]
    heapq.heappush(q, [0,1])
    distance[1] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost,i[0]])
    
    count = 0
    for i in distance:
        if i <= K:
            count += 1
    return count


#Point
#다익스트라 문제
