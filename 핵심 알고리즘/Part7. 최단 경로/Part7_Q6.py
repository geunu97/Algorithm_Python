#Part7. 최단 경로
#문제 6. 1~번까지 헛간과, 헛간 사이에는 M개의 양방향 통로가 있다. 술래가 1번에서 출발하여 가장 최단거리가 먼 헛간과(여러개면 가장 작은 헛간 번호), 
#        그 헛간까지의 최단거리와, 그 헛간과 같은 최단거리를 갖는 헛간의 개수 구하기 
#        여기서 최단거리란 지나야 하는 통로의 최소 개수를 의미

import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append([b,1])
    graph[b].append([a,1])

INF = 987654321
distance = [INF] * (N+1)

q = []
heapq.heappush(q, [0,1])  #거리, 시작점
distance[1] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]: 
        cost = dist + i[1]  #연결되어있는 것 불러와서 cost는 (시작점->now->now와 연결된 노드)까지 거리

        if cost < distance[i[0]]:  #이미 그 노드 최단거리 계산 된것보다 cost가 더 작다면
            distance[i[0]] = cost  #최단거리 갱신
            heapq.heappush(q,[cost,i[0]])


max_node = 0
max_distance = 0
result = []

for i in range(1, N+1):
    if max_distance < distance[i]: #최댓값 찾기
        max_node = i  #헛간 번호
        max_distance = distance[i] #최단거리
        result = [max_node] 
    elif max_distance == distance[i]: 
        result.append(i)

print(max_node, max_distance, len(result))



#Point
#모든 간선은 1이다
#일반적인 다익스트라 문제