#Part7. 최단 경로
#문제 1. 1번 ~ N번까지의 회사가 있고 M개의 도로가 있다. 도로는 양방향으로 이동할 수 있으며 모든 도로는 1만큼 시간이 걸린다
#        1번에서 시작하여 K번 회사를 거쳐 X번 회사로 가는 최소 시간을 구하기

N,M = map(int,input().split())

#인접행렬로 그래프 그리기
INF = 987654321
graph = [ [INF]*(N+1) for _ in range(N+1) ] #무한으로 초기화   #graph[1][2]는 1에서2까지 가는 최단거리

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1  #양방향 간선으로 값 넣기

X,K = map(int,input().split())

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:   #자기자신의 최단거리 0 (대각선)
            graph[i][j] = 0

#3중 반복문 + 점화식 (플로이드 워셜 핵심!)
for i in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])   #핵심 (원리 notion보기)

if graph[1][K] + graph[K][X] >= INF:   #갈 수 없는 경우
    print('-1')
else:
    print(graph[1][K] + graph[K][X])  #더해주면 됨 


#Point
#플로이드 워셜 문제
#(1번에서 K번 인덱스) + (K번에서 X번 인덱스) 더해주면 됨
