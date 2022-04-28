#Part2. 구현
#문제 8. (구현/완전탐색) 2020 카카오 LV3 자물쇠와 열쇠

#2차원리스트 90도 회전시키는 함수                   
def rotate_a_matrix_by_90_degree(a):
    n = len(a)   #행길이
    m = len(a[0])  #열길이
    
    result = [[0] * n for _ in range(m)] #행열길이 반대로 0으로 초기화
    for i in range(n):          #값 위치 바꿔서 집어넣기
        for j in range(m):
            result[j][n-i-1] = a[i][j]     
    return result

#자물쇠 중간 부분이 모두 1인지 확인하는 함수
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    #자물쇠의 크기를 기존의 3배크기로 바꾸기
    new_lock = [[0]*(n*3) for _ in range(n*3)]  #먼저 크기에 맞게 0으로 초기화
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]    #가운데 부분에 원래 값 넣기
            
    #90도 회전 (4번)
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):      #x,y는 칸 이동
            for y in range(n*2):
                #자물쇠에 열쇠 끼워 넣기   (i,j는 현재 칸에 열쇠칸만 모두 집어넣기)
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                #정확히 열쇠가 맞는지 검사하기
                if check(new_lock) == True:
                    return True
                #자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False



#자물쇠 크기 3배로 늘려서 모두 한번씩 시도해본 후 
#90도 돌려서 똑같이 모두 시도 (4번 반복)

#가운데 부분이 모두 1이면 열쇠에 맞는 것


