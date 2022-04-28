#25단계: 최단 경로
#3. 사이클, 1번~V개의 마을과 한방향으로 된 E개의 도로가 있다. 운동을 시작점에서 시작한 후 도착점에 들렸다가 다시 시작점으로 돌아오려고 할 때
#   사이클이 가장 작은 거리의 합을 구해라.  (a,b,c) a에서 b로 갈 때 가중치 c  주어짐

V,E = map(int,input().split())

INF = 987654321
graph =[[INF]*(V+1) for _ in range(V+1)]

for i in range(1,V+1):
    for j in range(1,V+1):
        if i== j:
            graph[i][j] = 0

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for i in range(1,V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])
#위에는 동일

#같은 인덱스 제외하고 왕복 거리합 최솟값 찾기 (ex) graph[12] + graph[21])
min_value = 987654321
for i in range(1, V+1):
    result = 0
    for j in range(1, V+1):
        if i != j:
            result = graph[i][j] + graph[j][i]
            min_value = min(min_value, result)

if min_value == 987654321:  #사이클 할 수 없는 경우
    print('-1')
else:
    print(min_value)


#Point
#범위가 작기 때문에 플로이드 워셜 사용