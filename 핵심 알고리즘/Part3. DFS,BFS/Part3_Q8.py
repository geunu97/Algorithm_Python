#Part3. DFS,BFS
#문제 8. (BFS)  인구이동 (백준 16234)

#pass
'''
from collections import deque

N,L,R = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))


q = []
q = deque(q)

for x in range(N):
    for y in range(N):
        q.append([graph[x][y],x,y])

        sum = 0
        while q:
            value,x,y = q.popleft()
            sum += value

            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < N and ny >=0 and ny < N:
                    if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                        q.append([graph[nx][ny],nx,ny])
'''






