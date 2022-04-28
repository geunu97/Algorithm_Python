#24단계: DFS와 BFS
#1. 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하기 (정점 번호가 작은 것을 먼저 방문)
# 4 5 1  #정점의 개수, 간선의 개수, 탐색 시작할 정점의 번호
# 1 2  #연결된 간선 (양방향)
# 1 3
# 1 4
# 2 4
# 3 4

from collections import deque

N,M,V = map(int,input().split())

graph = [ [] for _ in range(N+1)]           #인접리스트로 그래프 그리기 (양방향)  // # 1부터 시작이니깐 1개 더 받기
for i in range(1,M+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a] = sorted(graph[a])
    graph[b] = sorted(graph[b])

answer_DFS = []                             #DFS
answer_DFS.append(V)
def DFS(V):
    for i in graph[V]:  #해당 번호에 연결된 곳 불러오기
        if i not in answer_DFS:
            answer_DFS.append(i)
            DFS(i)
            
answer_BFS = []                             #BFS
answer_BFS.append(V)
q = deque(answer_BFS)
q.append(V)
def BFS(q):
    while q:
        value = q.popleft()

        for i in graph[value]:
            if i not in answer_BFS:
                answer_BFS.append(i)
                q.append(i)

DFS(V)
BFS(q)

for i in range(len(answer_DFS)):
    print(answer_DFS[i],end=" ")

print("")
for i in range(len(answer_BFS)):
    print(answer_BFS[i],end=" ")