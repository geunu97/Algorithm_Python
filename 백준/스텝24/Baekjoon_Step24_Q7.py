#24단계: DFS와 BFS
#7. 이전과 같은 문제지만 3차원 문제 (높이,행,열)

from collections import deque

M,N,H = map(int,input().split())

list_1 = []

graph =  [[[0] * M for _ in range(N)] for _ in range(H)]            #3차원 입력받기 (이렇게 받아야만 복사안됨)
for i in range(H):
    for j in range(N):
        list_a = list(map(int,input().split()))

        for k in range(M):
            graph[i][j][k] = list_a[k]

            if graph[i][j][k] == 1:
                list_1.append([i,j,k,0]) #시간도 같이 넣기

dz = [0,0,0,0,1,-1]
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]

q = deque(list_1)  #여러개 변수로 받기 위해선 꼭 안에 있는건 이중리스트여야됨 

while q:
    z,y,x,time = q.popleft()

    for i in range(6):   #상 하 좌 우 위 아래 (6가지)
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if nx >= 0 and nx < M and ny >= 0 and ny < N and nz >= 0 and nz < H:  #공간 벗어나는 경우 6가지
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                q.append([nz,ny,nx,time+1])

check = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                check = 1
                print('-1')
                exit()

if check != 1:
    print(time)





#Point
#BFS & 3차원