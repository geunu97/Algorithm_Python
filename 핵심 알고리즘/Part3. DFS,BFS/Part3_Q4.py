#Part3. DFS,BFS
#문제 4. (DFS) 0,1,2구성된 N*M 크기의 직사각형에서 벽3개를 설치하여 바이러스가 최소로 퍼질 때 구하기 (백준 14502)

from itertools import combinations       #풀었다!@#$!@$!@%!@%!!@#!@#@!#!@#!@#!@3

n,m = map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

list_0s = []      #0이라면 해당 인덱스들 [i,j] 형태로 모두 모으기
list_2s = []      #2이라면 해당 인덱스들 [i,j] 형태로 모두 모으기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            list_0s.append([i,j])
        elif graph[i][j] == 2:
            list_2s.append([i,j])

combinations_ = list(combinations(list_0s,3))

def DFS(x2,y2):   #DFS()에서 상하좌우 문제니깐 (시작점, dx,dy , nx,ny + 재귀) 사용해도 됨

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x2 + dx[i]
        ny = y2 + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:         #공간 안에서
            if list_new[nx][ny] == 0:                  #0일때만 2넣기 //다른 조건 필요없음
                list_new[nx][ny] = 2
                DFS(nx,ny)

max_value = -987654321
for list_0 in combinations_:
    list_new = [[0]*m for _ in range(n)]  #매번 새로 하나 더 만들기
    for i in range(n):
        for j in range(m):
            list_new[i][j] = graph[i][j]  #이런식으로 값을 하나하나 넣어야 graph값이 안바뀜!!!!!!!!!! 중요!!!!!   #list_new = graph 절대안됨!!!

    for x,y in list_0:      #이 표현도 외우기 (벽 세우기)
        list_new[x][y] = 1
        
    for x2,y2 in list_2s:  #이 표현도 외우기 (2에서만 시작)
        DFS(x2,y2)

    count = 0
    for i in range(n):
        for j in range(m):
            if list_new[i][j] == 0:           #이런식으로 0 세기
                count += 1

    max_value = max(count,max_value)

print(max_value)


#Point
#조합 & DFS 
#전체 다 다시 천천히 보기(모두 중요!)

