#24단계: DFS와 BFS
#9.  벽은 1번 부술 수 있을 때 (1, 1)에서 (N, M)의 위치까지의 최소 이동 횟수를 구해라 (최단 경로)

from collections import deque

N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))

distance = [[[0] * 2 for _ in range(M)] for _ in range(N)]     #최단거리 리스트 만들어주기 & 벽 부술수 있는 개수 나타내기  (3중 리스트)
distance[0][0][1] = 1   #시작점 & 벽 1번 부술 수 있음 = 1


dx = [-1,1,0,0]
dy = [0,0,1,-1]

def BFS():
    q = deque([[0,0,1]])     #[시작점,벽한번부술수 있는 기회] -> [x,y,1]   시작

    while q:
        x,y,wall = q.popleft()

        if x == N-1 and y == M-1:
            return distance[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if graph[nx][ny] == 1 and wall == 1:  #벽을 만났고 뚫을수 있는 상태라면
                    distance[nx][ny][0] = distance[x][y][1] + 1  #거리+1씩 해주고 벽 부술수 있는 기회 0으로 바꿔주기
                    q.append([nx,ny,0])   # 벽 부술수 있는 기회 0으로 바꿔주기

                elif graph[nx][ny] == 0 and distance[nx][ny][wall] == 0:  #갈 수 있는 곳이고 아직 방문하지 않았다면
                    distance[nx][ny][wall] = distance[x][y][wall] + 1 #벽상태는 그대로, 거리 + 1만 해주기
                    q.append([nx,ny,wall])

    return -1                 

print(BFS())

#Point
#BFS
#최단거리 & 벽 1개 부수기 문제
#가는길에 벽을 만났을 때 부수기 , 3중 리스트로 풀기
