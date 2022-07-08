from collections import deque

N,M = map(int,input().split())
graph = []
for _ in range(N):
  graph.append(list(map(int,input().split())))

move = deque([])
for _ in range(M):
  a,b = map(int,input().split())
  move.append([a,b])

dx = [ 0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1,  0,  1, 1, 1, 0, -1]

start_cloud = [[N,1],[N,2],[N-1,1],[N-1,2]]

while move:
  a,b = move.popleft()

  #구름이동
  for i in range(len(start_cloud)):
    x = start_cloud[i][0]
    y = start_cloud[i][1]
    for _ in range(b):
      nx = x + dx[a-1]
      ny = y + dy[a-1]

      if nx == 0:
        nx = N
      elif nx == N+1:
        nx = 1
      if ny == 0:
        ny = N
      elif ny == N+1:
        ny = 1
      
      x = nx
      y = ny
    
    start_cloud[i] = [x,y]
  

  for x2,y2 in start_cloud:
    #1씩 비내리기
    graph[x2-1][y2-1] += 1

  for x2,y2 in start_cloud:
    #물복사버그 마법 시전
    count = 0
    if 0 <= x2-2 < N and 0 <= y2-2 < N:    #대각선 왼쪽위
      if graph[x2-2][y2-2] > 0:
        count += 1
    
    if 0 <= x2 < N and 0 <= y2-2 < N:      #대각선 왼쪽아래
      if graph[x2][y2-2] > 0:
        count += 1
    
    if 0 <= x2-2 < N and 0 <= y2 < N:      #대각선 오른쪽위
      if graph[x2-2][y2] > 0:
        count += 1

    if 0 <= x2 < N and 0 <= y2 < N:        #대각선 오른쪽아래
      if graph[x2][y2] > 0:
        count += 1

    graph[x2-1][y2-1] += count
  
  dictionary = {}
  for cloud in start_cloud:
    dictionary[" ".join([str(cloud[0]),str(cloud[1])])] = 1

  #물의 양 2이상인 모든 칸 구름 생기고, 물의 양 2줄이기
  new_cloud = []
  for x3 in range(N):
    for y3 in range(N):
      if graph[x3][y3] >= 2:
        if " ".join([str(x3+1),str(y3+1)]) not in dictionary:
          graph[x3][y3] -= 2
          new_cloud.append([x3+1,y3+1])

  #구름 초기화
  start_cloud = []
  for cloud in new_cloud:
    start_cloud.append(cloud)
  

answer = 0
for x4 in range(N):
  for y4 in range(N):
    answer += graph[x4][y4]

print(answer)
