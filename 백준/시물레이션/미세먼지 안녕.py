R,C,T = map(int,input().split())
graph = []
for _ in range(R):
  graph.append(list(map(int,input().split())))

dx = [0,0,1,-1]    
dy = [1,-1,0,0]
dx_top = [0,-1,0,1]   #오른쪽,위,왼쪽,아래
dy_top = [1,0,-1,0]
dx_bottom = [0,1,0,-1]   #오른쪽,아래,왼쪽,위
dy_bottom = [1,0,-1,0]

time = 0
#1초 반복
while True: 
  #공기청정기, 미세먼지 위치 확인
  air_cleaner = []
  dust = []
  for x in range(R):
    for y in range(C):
      if graph[x][y] == -1:
        air_cleaner.append([x,y])
      elif graph[x][y] != 0:
        dust.append([x,y])

  #1. 미세먼지 확산  (주의: 동시에 확산!!)
  new_graph = [[0] * C for _ in range(R)]
  for x2,y2 in dust:
    count = 0
    for i in range(4):
      nx = x2 + dx[i]
      ny = y2 + dy[i]

      if 0 <= nx < R and 0 <= ny < C:
        if graph[nx][ny] != -1:
          count += 1
          new_graph[nx][ny] += (graph[x2][y2] // 5)
    
    new_graph[x2][y2] += (graph[x2][y2] - graph[x2][y2] // 5 * count)
  
  #2. 공기청정기 작동                       
  #2-1. 공기청정기 위쪽 작동
  top_x = air_cleaner[0][0]
  top_y = air_cleaner[0][1]
  new_graph[top_x][top_y] = 0
  look = 0  #처음은 오른쪽 방향
  value = new_graph[top_x][top_y]
  while True:
    nx = top_x + dx_top[look]
    ny = top_y + dy_top[look]
    if 0 <= nx < R and 0 <= ny < C:
      next_value = new_graph[nx][ny]              #주의 (잘못하면 하나의 값만 이동할 수 있음)   #테두리 이동
      new_graph[nx][ny] = value
      value = next_value
      top_x = nx
      top_y = ny
    else:
      look += 1
    if nx == air_cleaner[0][0] and ny == air_cleaner[0][1]:
      break
  new_graph[air_cleaner[0][0]][air_cleaner[0][1]] = -1 

  #2-2. 공기청정기 아래쪽 작동
  bottom_x = air_cleaner[1][0]
  bottom_y = air_cleaner[1][1]
  new_graph[bottom_x][bottom_y] = 0
  look = 0  #처음은 오른쪽 방향
  value = new_graph[bottom_x][bottom_y]
  while True:
    nx = bottom_x + dx_bottom[look]
    ny = bottom_y + dy_bottom[look]
    if 0 <= nx < R and 0 <= ny < C:
      next_value = new_graph[nx][ny]
      new_graph[nx][ny] = value
      value = next_value

      bottom_x = nx
      bottom_y = ny
    else:
      look += 1
    if nx == air_cleaner[1][0] and ny == air_cleaner[1][1]:
      break
  new_graph[air_cleaner[1][0]][air_cleaner[1][1]] = -1 

  time += 1
  if time == T:
    break
  else:
    graph = [[0] * C for _ in range(R)]
    for x3 in range(R):
      for y3 in range(C):
        graph[x3][y3] = new_graph[x3][y3]

#결과
answer = 0
for x in range(R):
  for y in range(C):
    if new_graph[x][y] > 0:
      answer += new_graph[x][y]

print(answer)







