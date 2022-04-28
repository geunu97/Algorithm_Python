#25단계: 최단 경로
#2. 1번에서 N번으로 최단거리로 이동할 때, 1번부터 주어진 정점 x,y 2개를 반드시 거쳐 N번까지 이동할 때 최단거리 구하기, 
#   정점의 개수 N, 양방향 간선의 개수 E, (a,b,c) a에서 b로 갈 때 가중치 c 

import heapq
import sys
input = sys.stdin.readline

N,E = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

x,y = map(int,input().split())

INF = 987654321
result_distance = []
def Dijkstra(start):
    distance = [INF] * (N+1)

    q = []
    heapq.heappush(q, [0,start])
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost,i[0]])

    result_distance.append(distance)

Dijkstra(1) #1번출발
Dijkstra(x) #x번출발
Dijkstra(y) #y번출발

answer = min(result_distance[0][x] + result_distance[1][y] + result_distance[2][N], result_distance[0][y] + result_distance[2][x] + result_distance[1][N])

if answer >= INF: #갈 수 없을 때
    print('-1')
else:
    print(answer)



#Point
#범위가 크기 때문에 다익스트라 알고리즘 사용

#출발점을 3번 구해 각각 더해주면 된다

#2가지로 나눌 수 있다 (이 중에서 최솟값 선택)
#1번에서 출발 + x에서 출발 + y에서 출발 
#1번에서 출발 + y에서 출발 + x에서 출발

#함수로 풀기