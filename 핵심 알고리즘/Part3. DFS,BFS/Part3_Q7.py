#Part3. DFS,BFS
#문제 7. (DFS) S,T,O로 구성된 N*M 직사각형에서 선생님은 상하좌우로로만 볼수 있을 때 장애물을 이용해 학생들이 선생님의 감시피하기 (백준 18428)

from itertools import combinations  #헐 풀었다...? 왜 풀렸지...?

N = int(input())
graph = []
for i in range(N):
    graph.append(list(input().split()))

list_T=[]
list_X=[]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            list_X.append([i,j])
        elif graph[i][j] == 'T':
            list_T.append([i,j])

combi_s = list(combinations(list_X,3))
check = -1
def DFS(list_new,x2,y2,i):
    global check

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    nx = x2 + dx[i]
    ny = y2 + dy[i]

    if nx >= 0 and nx < N and ny >= 0 and ny < N:
        if list_new[nx][ny] == 'O':
            return
        elif list_new[nx][ny] == 'X':
            DFS(list_new,nx,ny,i)
        elif list_new[nx][ny] == 'S':
            check = 1
            return 

finish = 0
for combi in combi_s:
    check = -1

    list_new = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            list_new[i][j] = graph[i][j]

    for x,y in combi:
        list_new[x][y] = 'O'

    for x2,y2 in list_T:
        for i in range(4):
            DFS(list_new,x2,y2,i)
    
    if check == -1:
        finish = 1
        print("YES")
        break

if finish != 1:
    print("NO")


#Point
#조합 & DFS