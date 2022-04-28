#24단계: DFS와 BFS
#3. 정사각형 모양에서. 1은 집, 0은 집이 없는 곳을 나타날때 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다
#   지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 구하기

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
def DFS(x,y):
    global count

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >=0 and ny < N:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0    #방문 처리
                count += 1
                DFS(nx,ny)

answer_count = []

for x in range(N):    #모든 좌표에서 시작
    for y in range(N):
        if graph[x][y] != 0:
            count = 1
            graph[x][y] = 0
            DFS(x,y)

            answer_count.append(count)

answer_count = sorted(answer_count)

print(len(answer_count))
for i in answer_count:
    print(i)


#Point
#이전 얼음틀 문제와 매우 비슷
#DFS