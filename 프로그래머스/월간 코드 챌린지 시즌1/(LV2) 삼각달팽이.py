#LV2 삼각달팽이
'''
def solution(n):
    maps = [[0]*n for _ in range(n)]   #2차원 그래프 그리기
    
    num = 0
    mode = [[1, 0], [0, 1], [-1, -1]]  #방향(아래 , -> , 왼쪽대각선위)
    x, y, m = -1, 0, 0   #현재좌표, 바라보는방향

    while n > 0 :
        for _ in range(n) :
            x += mode[m%3][0]
            y += mode[m%3][1]
            num += 1  #넣을 값, 1씩 증가
            maps[x][y] = num

        m += 1  #방향 바꾸기
        n -= 1  #총 n번 실행하기 


    answer = []
    count = 0
    for i in maps:   #2중리스트에서 삼각형처럼 뽑아내기 (1개..2개..3개..)
        answer += i[:count+1]
        count += 1

    return answer


print(solution(4))
'''

#2번째 풀이

def solution(n):
    #삼각형 그래프 초기화
    number = 1
    graph = []
    for i in range(n):
        graph.append([0] * number)
        number += 1
    
    #3가지 방향 좌표
    top_bottom = [1,0]
    left_right = [0,1]
    bottom_top = [-1,-1]
    
    number = 1
    count = 0   
    nn = n
    
    x = -1
    y = 0
    
    while True:
        
        for _ in range(n):
            x = x + top_bottom[0]
            y = y + top_bottom[1]
            
            graph[x][y] = number
            number += 1
            
        count += 1
        n -= 1
            
        if count == nn:
            break

        for _ in range(n):
            x = x + left_right[0]
            y = y + left_right[1]   
            
            graph[x][y] = number
            number += 1
            
        count += 1
        n -= 1

        if count == nn:
            break
            
        for _ in range(n):
            x = x + bottom_top[0]
            y = y + bottom_top[1]  
        
            graph[x][y] = number
            number += 1
            
        count += 1
        n -= 1
        
        if count == nn:
            break
    
    answer = []
    for i in graph:
        for j in i :
            answer.append(j)
    
    return answer


#Point (시물레이션처럼 풀기)

#시작좌표 설정
#3가지 방향 설정 [1,0], [0,1], [-1,-1]
#한 방향당 n번씩 돌고, 방향 전환 후, n-1해주기  (4번..3번..2번..1번)
#한 방향 돌때마다 count+1해주고, 총 방향을 n번 만큼 실행 된다



