#LV2 문자열 압축

def solution(s):
    if len(s) == 1:    #예외
        return 1
    
    answer = []
    step = 1    #1단계부터 s의길이 반절까지만 계산 (자르는 갯수)
    while step <= len(s) // 2:
        count = 1
        result = ""
        value = ""   
        for i in range(0,len(s),step):
            if value == s[i:i+step]:
                count += 1
            else:
                if count != 1:
                    result += (str(count)+value)
                elif count == 1:
                    result += value
                    
                value = s[i:i+step]
                count = 1
        
        #마지막 남은거 처리
        if count != 1:
            result += (str(count)+value)
        elif count == 1:
            result += value
        
            
        answer.append(len(result))
        step += 1
                    
                
    return min(answer)