#24단계: DFS와 BFS
#10. 체스판 위에 나이트가 있을 때 나이트는 L자 형태로 움직일 수 있다. 출발점부터 도착점까지 몇번만에 이동할 수 있는지 구하기

from collections import deque

T = int(input())

for _ in range(T):
    I = int(input())

    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    
    distance = [[0] * I for _ in range(I)]  #거리 리스트 만들기!!!!!!!!!!

    dx = [1,-1,1,-1,2,2,-2,-2]
    dy = [2,2,-2,-2,1,-1,1,-1]

    q = deque([[a1,b1]])

    while q:
        x,y = q.popleft()

        if x == a2 and y == b2:   #도착점과 만나면 종료
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < I and ny >= 0 and ny < I:
                if distance[nx][ny] == 0:      #아직 방문한 곳이 아니라면
                    distance[nx][ny] = distance[x][y] + 1    
                    q.append([nx,ny])

    print(distance[a2][b2])


#Point
#BFS