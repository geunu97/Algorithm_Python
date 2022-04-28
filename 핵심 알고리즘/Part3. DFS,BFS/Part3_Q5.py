#Part3. DFS,BFS
#문제 5. (BFS) N*M크기 직사각형에서 1~K번까지 바이러스가 있을 때 가장 작은번호부터 가장 큰번호까지 1초에 인접한 칸 전염시키기

from collections import deque

N,K = map(int,input().split())
graph = []
list_index = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            list_index.append([i,j,graph[i][j],0])   #리스트에 시간도 같이 넣기

S,X,Y = map(int,input().split())

list_index = sorted(list_index,key = lambda x: x[2])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q = deque(list_index) #큐

#BFS 시작
while q:
    x,y,virus,time = q.popleft()

    if time == S: #시간되면 종료
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus   
                q.append([nx,ny,virus,time+1])  #큐에 시간도 같이 넣기!!!! 중요!! 시간되면 종료

print(graph[X-1][Y-1])

#Point
#인접한 것들만 한번 계산이기 때문에 BFS() 
