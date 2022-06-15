from collections import deque 

def solution(places):
    dx = [0,0,1,-1] 
    dy = [1,-1,0,0]   
    
    answer = []
    for i in range(5):
        person = []
        graph = [[0] * 5 for _ in range(5)]      #그래프 초기화
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    person.append([j,k])         #사람 위치 받기
                graph[j][k] = places[i][j][k]
        
        result = True
        for x,y in person:
            graph[x][y] = 0
            
            q = deque([[x,y]])     #bfs
            while q:
                x,y = q.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if graph[x][y] + 1 <= 2:   #거리 2이내만 계산
                            if graph[nx][ny] == 'O':
                                graph[nx][ny] = graph[x][y] + 1
                                q.append([nx,ny])
                            elif graph[nx][ny] == 'P':    #도중에 P만나면 안됨
                                result = False
        
        if result:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer

  
#문제: (거리두기 문제) 사람과 사람 거리가 2이내라면 False, 대신 거리 2이내인데 칸막이가 존재하면 괜찮다

#bfs
'''
1. 그래프에서 모든 사람의 위치(인덱스)를 구합니다

2. 모든 사람이 위치하는 곳을 시작점으로 하여 상하좌우로 인접한 칸을 bfs를 활용하여 나아갑니다
  - 이 때, 거리 2이내까지만 계산하면 됩니다

3. bfs를 활용하여 다음 칸으로 가기 위한 조건은 다음과 같습니다
  - 다음 칸이 O(빈 테이블)이고 거리가 2이내라면 나아갑니다   
  - 다음 칸이 P(사람)이고, 거리가 2이내라면 False를 반환합니다  
'''