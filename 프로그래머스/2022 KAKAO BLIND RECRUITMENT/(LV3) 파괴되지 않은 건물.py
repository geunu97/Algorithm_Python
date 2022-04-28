#LV3 파괴되지 않은 건물

def solution(board, skill):
    N = len(board)  #열
    M = len(board[0])  #행
    
    graph = [[0] * (M+1) for _ in range(N+1)]
    
    for type,x1,y1,x2,y2,degree in skill:
        if type == 1:
            degree = -degree
        
        graph[x1][y1] += degree
        graph[x1][y2+1] += -degree  
        graph[x2+1][y1] += -degree  
        graph[x2+1][y2+1] += degree 
    
    
    #왼쪽에서 오른쪽으로 하나씩 누적합
    for i in range(N+1):
        for j in range(M):
            graph[i][j+1] += graph[i][j] 
        
    #위에서 아래쪽으로 하나씩 누적합
    for i in range(N):
        for j in range(M+1):
            graph[i+1][j] += graph[i][j]  
    
    
    answer = 0
    #이제 board와 합치고, 답 구하기
    for i in range(N):
        for j in range(M):
            board[i][j] += graph[i][j] 
            
            if board[i][j] > 0:
                answer += 1
    
    
    #print(board)
        
    return answer

#2차원 누적합 응용문제 
#해설보기 https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

