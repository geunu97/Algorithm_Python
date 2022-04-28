#24단계: DFS와 BFS
#5. (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하기

from collections import deque

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque([[0,0]])   #시작점   #이중리스트로 해줘야 x,y로 받을 수 있음  #단일리스트일 경우 x,y로 받을 때오류남

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1          # 실수!! +=이게 아님    #통로의 값이 모두 동일하기 때문에 1씩 더해주면서 나아가면 됨   
                q.append([nx,ny])
        
print(graph[N-1][M-1])

#Point
#BFS
#이전에 풀었던 문제와 매우 비슷