#Part7. 최단 경로
#문제 5. N*N크기에서 각각의 칸을 지나기 위한 비용이 주어질 때 시작위치(0,0)에서 도착위치(N-1,N-1)까지 최소 비용 출력하기, 이동은 상하좌우 1칸씩 이동할 수 있다.

import heapq
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

T = int(input())
for _ in range(T):
    N = int(input())

    INF = 987654321
    graph = []
    for _ in range(N):
        graph.append(list(map(int,input().split())))

    distance = [[INF]*N for _ in range(N)]  #최단거리 리스트 무한으로 초기화

    x = 0  #시작위치
    y = 0
    q = [[graph[x][y], x,y]]    #(비용,위치) 넣기
    distance[x][y] = graph[x][y]  #시작점

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx>= N or ny < 0 or ny >= N:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, [cost,nx,ny]) 

    print(distance[N-1][N-1])


#Point 
#변형된 다익스트라 알고리즘 문제 

