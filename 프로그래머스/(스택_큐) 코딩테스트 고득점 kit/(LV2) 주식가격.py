#LV2 주식가격

def solution(prices):
    answer = []
    
    for i in range(len(prices)-1):
        check = 0
        value = prices[i]
        
        for j in range(i+1,len(prices)):
            if value > prices[j]:
                answer.append(j-i)
                check = 1
                break
        
        if check == 0:
            answer.append(len(prices)-1-i)
            
            
    answer.append(0)
    return answer