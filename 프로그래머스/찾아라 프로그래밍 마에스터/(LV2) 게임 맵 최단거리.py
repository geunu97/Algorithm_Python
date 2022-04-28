#LV2 게임 맵 최단거리

from collections import deque

def solution(maps):
    m = len(maps[0])
    n = len(maps)
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque([[0,0]])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append([nx,ny])
    
    if maps[-1][-1] == 0 or maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


#Point
#BFS 문제, 최단거리 문제, 이전 미로탈출 문제와 같은문제, 기본 문제

