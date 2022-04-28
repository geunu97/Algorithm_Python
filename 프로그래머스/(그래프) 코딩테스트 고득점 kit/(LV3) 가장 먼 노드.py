#LV3 가장 먼 노드

import heapq

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a,b in edge:
        graph[a].append([b,1])
        graph[b].append([a,1])
    
    start = 1
    INF = 987654321
    distance = [INF] * (n+1)
    
    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
    
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

    #print(distance)
    answer = 0
    for i in distance:
        if i != INF and i == max(distance[1:]):
            answer += 1
    
    return answer

#Point
#기본 다익스트라 알고리즘 문제