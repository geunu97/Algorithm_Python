#25단계: 최단 경로
#1. 주어진 시작점에서 다른 모든 정점으로의 최단 거리 구하기. 정점의 개수 V, 간선의 개수 E, 시작점 K, (u,v,w) u에서 v로 가는 w가중치 주어짐

import heapq
import sys
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

INF = 987654321
distance = [INF] * (V+1)

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

for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])


#Point
#다익스트라 알고리즘