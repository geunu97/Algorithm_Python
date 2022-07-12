from collections import deque

N,M,K = map(int,input().split())


graph = [[deque([]) for _ in range(N)] for _ in range(N)]    #핵심
command = []
for _ in range(M):
  x,y,m,s,d = map(int,input().split()) #위치x,위치y, 질량,속력,방향  

  graph[x-1][y-1].append([m,s,d])
  command.append([x-1,y-1,m,s,d])

#8가지 방향
dx = [-1,-1, 0, 1, 1,  1, 0,  -1]
dy = [ 0, 1, 1, 1, 0, -1, -1, -1]


count_k = 0
while True:
  #모든 파이어볼 이동하기
  for x,y,m,s,d in command:
    graph[x][y].popleft()

    count = 0
    while True:
      nx = x + dx[d]   #가짜 이동
      ny = y + dy[d]

      #그래프 이어져 있음
      if nx == N:
        nx = 0
      elif nx == -1:
        nx = N-1
      if ny == N:
        ny = 0
      elif ny == -1:
        ny = N-1
      
      x = nx   #진짜 이동
      y = ny
      
      count += 1
      if count == s:
        graph[x][y].append([m,s,d])
        break

  command = []
  #파이어볼이 2개 이상인 곳 찾기   
  for x2 in range(N):
    for y2 in range(N):
      if len(graph[x2][y2]) >= 2:
        sum_m = 0
        sum_s = 0
        sum_d_odd = 0
        sum_d_even = 0
        for fireball in graph[x2][y2]:
          sum_m += fireball[0]
          sum_s += fireball[1]
          if fireball[2] % 2 == 0:
            sum_d_even += 1
          else:
            sum_d_odd += 1

        sum_m = sum_m // 5
        sum_s = sum_s // len(graph[x2][y2])
        if sum_d_even == len(graph[x2][y2]) or sum_d_odd == len(graph[x2][y2]):
          if sum_m != 0:
            command.append([x2,y2,sum_m,sum_s,0])
            command.append([x2,y2,sum_m,sum_s,2])
            command.append([x2,y2,sum_m,sum_s,4])
            command.append([x2,y2,sum_m,sum_s,6])
            graph[x2][y2] = deque([[sum_m,sum_s,0],[sum_m,sum_s,2],[sum_m,sum_s,4],[sum_m,sum_s,6]])
          else:
            graph[x2][y2] = deque([])
        else:
          if sum_m != 0:
            command.append([x2,y2,sum_m,sum_s,1])
            command.append([x2,y2,sum_m,sum_s,3])
            command.append([x2,y2,sum_m,sum_s,5])
            command.append([x2,y2,sum_m,sum_s,7])
            graph[x2][y2] = deque([[sum_m,sum_s,1],[sum_m,sum_s,3],[sum_m,sum_s,5],[sum_m,sum_s,7]])
          else:
            graph[x2][y2] = deque([])
      elif len(graph[x2][y2]) == 1:
        for m,s,d in graph[x2][y2]:
          command.append([x2,y2,m,s,d])
      
  count_k += 1
  if count_k == K:
    break


answer = 0
for x in range(N):
  for y in range(N):
    while graph[x][y]:
      result = graph[x][y].popleft()
      answer += result[0]

print(answer)




#핵심
#2차원 그래프  #큐   #각 칸 여러개
'''
graph = [[deque([]) for _ in range(N)] for _ in range(N)] 
'''
