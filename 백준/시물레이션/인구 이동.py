from collections import deque
import sys
sys.setrecursionlimit(10**5)   #예외 처리 필수

N,L,R = map(int,input().split())
graph = []
for i in range(N):
  graph.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def re(day):
  new_graph = [[0] * N for _ in range(N)]    #국경선 표시를 위해 새로운 그래프 이용
  count = 1
  result = []
  #국경선 열기
  for x in range(N):
    for y in range(N):
      if new_graph[x][y] == 0:
        new_graph[x][y] = count
        result2 = [[x,y]]
        q = deque([[x,y]])
        while q:   #bfs
          x2,y2 = q.popleft()

          for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
              if new_graph[nx][ny] == 0:
                if L <= abs(graph[x2][y2] - graph[nx][ny]) <= R:
                    new_graph[nx][ny] = new_graph[x2][y2]
                    result2.append([nx,ny])
                    q.append([nx,ny])

        if len(result2) >= 2:
          result.append(result2)

      count += 1

  #국경선 연 곳 평균값 넣기 (인구이동)
  for res in result:
    sum_value = 0
    for x,y in res:
      sum_value += graph[x][y]
    
    for x,y in res:
      graph[x][y] = sum_value // len(res)
  

  #확인
  check_count = 0
  result = True
  for x in range(N):
    for y in range(N):
      check_count += 1
      if new_graph[x][y] != check_count:
        result = False
        break

  if result == False:
    re(day+1)
  else:
    print(day)


re(0)  

'''
1. bfs를 이용하여 상하좌우 인접한 곳에 있는 값의 차이에 따라 국경선 여는 것을 아래와 같이 표시하였습니다
  - 국경선 표시를 위해 새로운 그래프 사용, 국경선을 열었다는 것은 같은 값으로 표현했습니다
    1, 1, 2, 3
    1, 2, 2, 4
    1, 5, 6, 7
 2. 1번 과정에서 같은 값을 가지는(국경선을 공유하는)곳에 값의 평균값(인구 이동)을 넣어줍니다
 3. 1일 간격으로 1번, 2번과정을 반복하는데, 국경선을 여는 곳이 없다면 종료합니다
'''
