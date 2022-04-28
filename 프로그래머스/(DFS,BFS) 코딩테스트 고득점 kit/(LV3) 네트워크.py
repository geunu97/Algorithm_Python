#LV3 네트워크

def dfs(num,graph,visited):
    for i in graph[num]:
        if visited[i] == 0:
            visited[i] = 1   #방문처리
            dfs(i,graph,visited)

def solution(n, computers):
    graph = [[] for _ in range(n+1)]          #인접리스트로 만들기
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i+1].append(j+1)  
                 
    visited = [0] * (n+1)    #방문처리 위함            
    answer = 0
    for num in range(1,n+1):
        if visited[num] == 0:      #아직 안가본곳
            visited[num] = 1       #방문처리
            dfs(num,graph,visited)  #재귀
            answer += 1
            
    return answer


#Point
#dfs문제 
#이전에 비슷한 문제 풀었었음


