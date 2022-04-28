#24단계: DFS와 BFS
#11. 이분 그래프 인지 아닌지 구하기

from collections import deque     

def BFS(start):
    visited[start] = 1   #시작점 방문처리& 그룹값 1
    
    q = deque([start])

    while q:
        now = q.popleft()

        for i in graph[now]: #해당 노드와 연결된 것 모두 불러오기
            if visited[i] == 0:  #연결된 곳이 아직 방문하지 않았다면
                visited[i] = -visited[now]    #연결된 곳은 모두 값이 달라야함
                q.append(i)
            else:                #연결된 곳이 이미 방문한 곳이라면
                if visited[i] == visited[now]:  #연결된 곳이 값이 같다면 이분그래프 아님
                    return False 
    return True 

k = int(input())

for _ in range(k):
    v, e = map(int,input().split())   

    graph = [[] for _ in range(v + 1)]   #인접리스트로 그래프 만들기    #1부터 시작이니깐 1개더 만들기
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)              #간선은 양방향

    visited = [0] * (v+1)   #방문 리스트 만들기   

    isTrue = True
    for k in range(1,v+1):   #1번 노드부터 시작  
        if visited[k] == 0:  #아직 방문 안했다면
            if not BFS(k):
                isTrue = False
                break
    if isTrue:
        print('YES')
    else:
        print('NO')


#Point
#BFS
#1번부터 아직 방문안한 곳들만 모두 따지고, 시작점부터 모두 연결되어 있는 것들은 (-붙여주기) 값이 달라야함
#연결되어 있는 값이 같다면 이분 그래프 아님
#연결되어 있는 값이 모두 다르다면 이분 그래프
#pypy3로 제출 or  import sys 해주기