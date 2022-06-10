from collections import deque

dx = [0,0,1,-1,1,-1,1,-1]
dy = [-1,1,0,0,1,-1,-1,1]

max_x = -987654321
max_y = -987654321

#(테두리 확인) 상하좌우대각선 7이 있는지 확인
def check_(i,j,graph):
    for z in range(8):
        nx = i + dx[z]
        ny = j + dy[z]
        
        if 0 <= nx < (max_y+1)*2 and 0 <= ny < (max_x+1)*2:
            if graph[nx][ny] == 7:
                return True
    
    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    global max_x 
    global max_y

    #(그래프 선언 하기 위해) x,y의 최댓값 확인    
    for a,b,c,d in rectangle:
        if c > max_x:
            max_x = c
        if d > max_y:
            max_y = d
    
    #그래프 선언
    graph = [[7] * ((max_x+1)*2) for _ in range((max_y+1)*2)]
    
    #사각형 2배 늘리기, 좌표점 2배로 나타내고, 좌표점 사이에 연결되어 있는 변도 1로 나타낼 수 있음
    for a,b,c,d in rectangle:
        for y in range(b*2,(d*2+1)):
            for x in range(a*2,(c*2+1)):
                graph[y][x] = 1
    
    #테두리 확인 및, 테두리는 0으로 변경하기
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                if check_(i,j,graph):
                    graph[i][j] = 0
                else:
                    graph[i][j] = 6
    
    #bfs로 시작점부터 0으로 연결되어 있는 점 모두 최단거리 구하기
    q = deque([[characterY*2,characterX*2]])
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < (max_y+1)*2 and 0 <= ny < (max_x+1)*2:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx,ny])
    
    #해당 값 구하고 2로 나누기    
    return graph[itemY*2][itemX*2] // 2


#Point
#그래프 2배로 선언
#사각형 2배로 늘려서, 그래프에 넣기

#(그래프 2배로 늘린 이유는) 예시1에서처럼 ㄷ자 모양에서 구별을 못한다
#(기존의 좌표점은 2배로 나타내고, 좌표점 사이사이에 연결되어 있는 변을 나타내기 위한 점이 있다고 생각하면 된다)
#좌표점과 연결되어 있는 변을 통해서만 이어지도록 bfs로 최단거리 구하면 된다

#나는 그래프에서 X축은 가로, Y축은 세로로 정의했다
#헷갈리지 않게 주의해야 한다

#여기서는 좌표문제인데, 인덱스 사용하기 쉽게 x,y (0,0)점이 인덱스 [0,0]과 똑같다 