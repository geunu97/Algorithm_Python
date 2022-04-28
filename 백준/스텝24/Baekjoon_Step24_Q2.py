#24단계: DFS와 BFS
#2. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
#   1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 구하기

N = int(input())
A = int(input())

virus = [0] * (N+1) #바이러스 리스트 만들어주기

graph = [ [] for _ in range(N+1)]     #인접리스트로 그래프 그리기 (양방향)  // # 1부터 시작이니깐 1개 더 받기
for i in range(A):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

virus[1] = -1
def DFS(v):
    for value in graph[v]:        #해당 번호에 연결된 곳 불러오기
        if virus[value] == 0:    
            virus[value] = -1
            DFS(value)            

DFS(1)
print(virus.count(-1)-1)

#Point
#DFS