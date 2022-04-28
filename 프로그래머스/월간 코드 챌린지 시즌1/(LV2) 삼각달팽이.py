#LV2 삼각달팽이

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



# https://blog.naver.com/handuelly/222157046417   (노트에 좌표 삼각형 그리기)

#Point
#삼각형을 직각삼각형으로 만든다.  -> 3가지 방향이 나온다
#3가지 방향에 대한 좌표 이용

