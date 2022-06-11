def solution(a):
    result = [False] * len(a)
    
    front = 99999999999
    end = 99999999999
    
    for i in range(len(a)):
        if a[i] < front:
            front = a[i]
            result[i] = True
        
        if a[-1-i] < end:
            end = a[-1-i]
            result[-1-i] = True
        
    return sum(result)


#투 포인터 문제
#다시 풀어보기
