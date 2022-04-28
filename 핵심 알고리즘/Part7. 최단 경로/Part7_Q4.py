#Part7. 최단 경로
#문제 4. N명의 학생과, 두 학생의 성적을 비교한 횟수 M번이 주어진다. 성적 순위를 정확히 알 수 있는 학생이 몇 명인지 구하기
#       (ex) 1 5가 주어지면 1번 학생은 5번 학생보다 성적이 낮다. 이와 같이 모두 비교를 통해 한 명의 학생이 정확히 몇등인지 알 수 있다) (386p)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

INF = 987654321
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

for i in range(1,N+1):
    for j in range(1, N+1):
        if i==j:
            graph[i][j] = 0

for i in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])


result = 0
for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == N:
        result += 1

print(result)

#Point
#플로이드 워셜 