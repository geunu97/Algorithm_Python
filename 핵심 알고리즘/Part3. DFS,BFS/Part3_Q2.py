#Part3. DFS,BFS
#문제 2. (BFS) 미로탈출 N*M 크기의 미로에서 (1,1)에서 시작하며, 0은 괴물 / 1은 통로 일 때 (N,M)에 출구가 있을 때 최소 이동 칸의 갯수는? (최단거리)

from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌 때까지 반복
    while queue: 
        x,y = queue.popleft()
        
        #주변 상 하 좌 우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #공간을 벗어나는 경우 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1    #총 몇번 걸렸는지 구하기 위해 +1씩 해주기
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(BFS(0,0))   #시작점 설정

#Point
#최단거리 문제시 BFS 사용
#시작점부터 큐에 넣고 시작 -> 값을 빼고 값을 뺀 곳에서 인접한 곳만(4방향) 탐색 -> 갈 수 있는 곳이면 값+1 해주고 -> 다음 칸 인덱스 큐에 넣기   //반복


