#Part7. 최단 경로
#문제 3. n개의 도시와, 도시에서 도시로 이동하는 m개의 버스가 있다. 버스를 이용할 때는 비용이 든다.
#        모든 도시 A에서 B로 가는데 비용의 최솟값 모두 구하기

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

#인접행렬로 그래프 만들기!!
INF = 987654321 
graph = [[INF]*(n+1) for _ in range(n+1)]  #무한으로 초기화!!
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)  #a에서 b에 대한 정보를 여러개(중복) 입력 받는 문제 (ex) 1 4 1 , 1 4 2)

#대각선 값 넣기!!
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#핵심!!
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

#최단거리 모두 출력하기
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0,end=" ") #i에서 j로 갈 수 없는 경우 0 출력 
        else:
            print(graph[i][j],end =" ") 
    print()


#Point
#기본적인 플로이드 워셜 문제