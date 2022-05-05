import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

min_value = 987654321
max_value = -987654321

graph = []
for i in range(n): 
    list_a = list(map(int,input().split()))
    min_value = min(min_value, min(list_a))
    max_value = max(max_value, max(list_a))
    graph.append(list_a)

def dfs(x2,y2,graph2):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x2 + dx[i]
        ny = y2 + dy[i]

        if 0 <= nx < n and 0 <= ny < n :
            if graph2[nx][ny] == 0:
                graph2[nx][ny] = 1
                dfs(nx,ny,graph2)


answer = -987654321
for i in range(min_value-1,max_value+1):
    graph2 = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if graph[x][y] <= i:
                graph2[x][y] = 1  #비에 젖은 지역 1

    count = 0
    for x2 in range(n):
        for y2 in range(n):
            if graph2[x2][y2] == 0:
                dfs(x2,y2,graph2)
                count += 1
  
    answer = max(answer, count)
  
print(answer)

#기본적인 dfs문제

#예외, 이 문제를 런타임 에러없이 풀기 위해서 무조건 sys.setrecursionlimit()를 추가해줘야 한다
#이 문제에서는 재귀가 엄청 깊게 진행되기 때문에, 어느 정도가 지나면 제한을 둬야하는 것이다