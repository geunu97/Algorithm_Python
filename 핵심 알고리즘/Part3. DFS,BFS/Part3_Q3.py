#Part3. DFS,BFS
#문제 3. (BFS) 1~N번까지의 도시와 M개의 단방향 도로가 존재할 때 출발점X에서부터 최단거리 K까지의 도시 구하기
#        (백준 18352) - pypy3로 제춣해서 성공 // python3 시간초과

from collections import deque

n,m,k,x = map(int,input().split())

#인접 리스트로 그래프 만들기!!
graph=[[] for _ in range(n+1)]  #1부터 시작이니깐 한개 더 받기
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

#모든 도시 최단거리 -1로 초기화 // 하나 더 만들기
distance = [-1] * (n+1)     #distance[1]은 1까지의 최단거리 // distance[2]은 2까지의 최단거리 ...
#출발도시는 최단거리 0
distance[x] = 0

#BFS 시작
#출발점부터 시작
q = deque([x])
while q:
  now = q.popleft()
  
  for next_node in graph[now]:    #시작점부터 연결되어 있는 모든 노드 불러오기
      if distance[next_node] == -1:  #연결되어 있는곳을 아직 방문하지 않았다면
          distance[next_node] = distance[now] + 1  #연결되어 있는 거리값에 현재 거리값 +1 씩 해주기 
          q.append(next_node)  #현재 점과 인접해있는 것 모두 q에 넣기

#최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:     #1부터 시작
        print(i)
        check = True

#만약 최단 거리가 K인 도시가 없다면 -1 출력
if check == False:
    print(-1)


#Point
#BFS

