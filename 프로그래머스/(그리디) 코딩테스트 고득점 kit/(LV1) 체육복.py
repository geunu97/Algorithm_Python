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

#2번쨰 풀이
def solution(n, lost, reserve):
    student = [0] * n
    
    for i in lost:
        student[i-1] += -1
    
    for i in reserve:
        student[i-1] += 1

    for i in range(len(student)):
        if student[i] == -1:
            if i == 0:
                if student[i+1] == 1:
                    student[i+1] = 0
                    student[i] = 0
            elif i == len(student)-1:
                if student[i-1] == 1:
                    student[i-1] = 0
                    student[i] = 0
            else:
                if student[i-1] == 1:
                    student[i-1] = 0
                    student[i] = 0
                elif student[i+1] == 1:
                    student[i+1] = 0
                    student[i] = 0
    
    
    return len(student) - student.count(-1)