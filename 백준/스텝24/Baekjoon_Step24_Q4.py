#24단계: DFS와 BFS
#4.어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다
#  배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 구하기

from collections import deque

T = int(input())

def BFS(x2,y2):             
    q.append([x2,y2]) #시작점

    while q:
        x2,y2 = q.popleft()

        for i in range(4):
            nx = x2 + dx[i]
            ny = y2 + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < M:    
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0          #방문처리!!
                    q.append([nx,ny])

for _ in range(T):
    M,N,K = map(int,input().split())

    graph = [ [0]* M for _ in range(N) ]
    
    for _ in range(K):
        a,b = map(int,input().split())
        graph[b][a] = 1                          #행 열 입력이 반대로 주어지는 문제

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    answer = 0
    q = deque()
    for x2 in range(N):        #모든 좌표에서 시작하기
        for y2 in range(M):
            if graph[x2][y2] == 1:
                BFS(x2,y2)
                answer += 1
    print(answer)


#Point 
#문제에서 인접 언급 BFS
#DFS로 풀면 맞는거 같은데 정답 판정이 안됨... BFS로 풀어서 정답판정 됨
#비슷하면서 다름!
    