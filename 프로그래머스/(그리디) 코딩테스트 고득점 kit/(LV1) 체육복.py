#LV1 체육복

def solution(n, lost, reserve):
    for i in range(1,n+1) :
        if i in lost and i in reserve:     #서로 같은 숫자 있으면 제거
            reserve.remove(i) 
            lost.remove(i)

    for i in range(1, n+1):
        if i in lost :    
            if i-1 in reserve :      #lost에 있는 숫자의 -1
                reserve.remove(i - 1)
                lost.remove(i)
                
            elif i+1 in reserve :    #lost에 있는 숫자의 +1
                reserve.remove(i + 1)
                lost.remove(i)

                
    return n - len(lost)