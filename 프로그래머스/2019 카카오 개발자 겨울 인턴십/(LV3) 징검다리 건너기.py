def solution(stones, k):
    left = 1
    right = 200000000
    
    answer = 987654321
    while left <= right:
        mid_value = (left + right) // 2
        
        count = 0  #연속된 갯수
        for i in stones:
            if i - mid_value <= 0:
                count += 1
                
            else:
                count = 0
            
            if count == k:
                break
        
        
        if count < k:
            left = mid_value + 1            
        
        else:
            answer = min(answer,mid_value)    #정답 중 최솟값 찾기 (모두 0이하의 값 연속된 갯수 k개 이상 만큼 된다)
            right = mid_value - 1
            
    
    return answer
    


#이진 탐색 문제!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! (이진 탐색 이구낭)

#정답(지나가는 횟수)을 탐색값으로 설정

#각 돌의 값에 탐색값 만큼 빼서, 연속된 0이하의 값 갯수 찾기    (연속된 0이하의 갯수가 k개이면 정답을 찾을 수 있다)




#다시 보기!!!!