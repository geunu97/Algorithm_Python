#Part3. DFS,BFS
#문제 1. (DFS) N*M 크기의 0,1로 구성된 얼음틀이 있을 때 연속된 0은 1개로 계산한다면 0의 갯수는 총 몇개인지 구하기   

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))


#연결된 모드 노드들 방문
def DFS(x,y):
    #주어진 범위를 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:  #0이라면 방문
        graph[x][y] = 1   #방문한 곳은 1로 바꿔주기
        #상,하,좌,우 위치 모두 재귀적 호출 (중요!!!)
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True   #0이 있는 공간은 True 반환
    return False  #0이 없다면 False 반환

result = 0
for i in range(n):
    for j in range(m):
        if DFS(i,j) == True: #모든 노드에서 출발
            result += 1

print(result)

#Point
#모든 좌표에서 시작
#시작점이 0이라면 -> 재귀함수 시작(시작점에서 상하좌우가 게속 0이라면 재귀로 구현)
#방문한 곳은 1로 바꿔주기!! 중요!!
#0의 공간이라면 True반환
#0이 없다면 False반환