import sys
sys.setrecursionlimit(100000)

m,n,k = map(int,input().split())

graph = [[0]*(n) for _ in range(m)]

for _ in range(k):
  x1,y1,x2,y2 = map(int,input().split())
  for x in range(x1,x2):
    for y in range(y1,y2):
      graph[y][x] = 1

result2 = 0
def dfs(x,y):
  global result2

  dx = [0,0,1,-1]
  dy = [1,-1,0,0]

  for r in range(4):
    nx = x + dx[r]
    ny = y + dy[r]

    if 0 <= nx < m  and 0 <= ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = 1
        result2 += 1
        dfs(nx,ny)


result1 = 0    # 영역 갯수
result3 = []
for x in range(m):
  for y in range(n):
    if graph[x][y] == 0:
      result2 = 1
      graph[x][y] = 1
      dfs(x,y)
      result3.append(result2)
      result1 += 1

result3 = sorted(result3)

print(result1)
for i in result3:
  print(i, end=" ")




# x,y 행열 헷갈리지 않게 주의!
# 기본적인 dfs 문제

#예외, 이 문제를 런타임 에러없이 풀기 위해서 무조건 sys.setrecursionlimit()를 추가해줘야 한다