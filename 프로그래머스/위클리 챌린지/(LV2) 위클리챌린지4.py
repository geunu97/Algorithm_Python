#LV2 전력망을 둘로 나누기

# n개의 탑에 서로 연결된 전선들이 주어진다. 이 때 특정번호와 특정번호가 연결된 전선1개만을 제거할 때 전선이 연결된 것끼리 2분할로 나누어진다. 
# 특정 전선1개를 잘 선택해서 제거하여 1분할 탑의 개수와 2분할 탑의 개수 차이가 최소가 되게 구해라  

from collections import deque

def dfs(num,visited,graph):
    for i in graph[num]:
        if visited[i] == 0: #아직 방문안했다면
            visited[i] = 1 #방문처리
            dfs(i,visited,graph) #dfs재귀 돌리기
            
    return visited
            
def solution(n, wires):
    answer = []

    wires = deque(wires) #큐
    for _ in range(n):
        x,y = wires.popleft()   #큐를 사용해서 한개씩 제거해주기 (n번)
        
        #인접리스트로 그래프 만들기
        graph = [[]for _ in range(n+1)]
        for a,b in wires:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0] * (n+1)  #방문처리 필수
        visited[1] = 1
        re_visited = dfs(1,visited,graph) #1번 노드만 확인해도 된다 // 1번과 연결된 노드들 & 나머지 연결된 노드들 (2분할)

        answer.append(abs(re_visited.count(0)-1 - re_visited.count(1))) #(2분할로 나눠진 노드들 갯수 차이)

        wires.append([x,y]) #다시 넣어주기
        
    return min(answer)

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))

#Point
#큐 & dfs(연결된 부분 찾기) 문제
#큐를 사용해서 1개씩 모두 제거하는 포인트 중요!!!

