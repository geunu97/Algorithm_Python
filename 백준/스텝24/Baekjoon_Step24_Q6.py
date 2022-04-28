#24단계: DFS와 BFS
#6. 하루에 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
#   며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하기     
#   1 익은 토마토  0 안 익은 토마토  -1 아무것도 없는 공간

from collections import deque

M,N = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

list_1 = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            list_1.append([x,y,0])   #출발점 모으기   #시간도 추가하기

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque(list_1)

while q:
    x,y,time = q.popleft()    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1   #방문 처리
                q.append([nx,ny,time+1])   #시간 +1씩 해주기

check = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            check = 1
            print('-1')
            exit()     #출력하고 나가줘야함   #실수...  #break는 반복문 하나탈출

if check != 1:
    print(time)



#Point
#출발점이 동시에 여러개 있는 문제 & 시간도 추가해줘서 푸는 문제
#BFS