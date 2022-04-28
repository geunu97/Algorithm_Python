#LV1 다트게임

def solution(dartResult):
    answer = [0,0,0]
    value = int(dartResult[0])   #처음 값 처리
    count = 0
    
    for i in range(1,len(dartResult)):
        if dartResult[i].isdigit(): 
            answer[count] = value
            count += 1
            
            if dartResult[i-1] == '1' and dartResult[i] == '0':    #1~10까지의 숫자중 10인지 판단하기
                value = 10
                count -= 1
            else:
                value = int(dartResult[i])
            
        elif dartResult[i] == 'S':
            value = value ** 1
        elif dartResult[i] == 'D':
            value = value ** 2
        elif dartResult[i] == 'T':
            value = value ** 3
        elif dartResult[i] == '*':
            if count == 0:
                value = value * 2
            else:
                answer[count-1] = answer[count-1] * 2
                value = value * 2
            
        elif dartResult[i] == '#':
            value = -value
    
    
    answer[2] = value   #끝처리
        
    return sum(answer)