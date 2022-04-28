#Part7. 최단 경로
#문제 2. N개의 도시와 한방향 간선 M개와 간선(시간)과 출발도시가 주어진다. 출발 도시에서 출발하여 연결된 다른 도시 모두에게 메시지를 보낼 때 
#       메시지를 받게 되는 도시의 총 개수와 도시들이 모두 메시지를 받는 데까지 걸리는 시간 구하기   

import heapq
import sys
input = sys.stdin.readline

N,M,start = map(int,input().split())
list_a = []
for _ in range(M):
    X,Y,Z = map(int,input().split())
    list_a.append([X,Y,Z])

#인접리스트로 그래프 만들기
graph = [ [] for _ in range(N+1) ]
for a,b,c in list_a:
    graph[a].append([b,c])  #a에서 b로 갈때 연결된 c간선

#최단거리 1차원 리스트 따로 만들어주기
INF = 987654321
distance = [INF] * (N+1) #무한으로 초기화

#시작(핵심) - (설명은 notion보기)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#시작
dijkstra(start)

#출발점에서 갈 수 있는 노드의 갯수
count = 0
#출발점부터 갈 수 있는 노드 중 가장 멀리있는 노드의 최단거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count -1, max_distance)



#Point
#개선된 다익스트라 알고리즘 사용