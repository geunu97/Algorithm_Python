#LV3 정수삼각형

def solution(triangle):
    dp = []      #dp테이블
    for i in range(1,len(triangle)+1):
        dp.append([0] * i)
    
    dp[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):    #보텀업
        for j in range(i+1):
            if j == 0:           #가장 왼쪽 그대로 내려오기
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif j == i:        #가장 오른쪽 그대로 내려오기
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:               #가운데는 , 위의 2개 중 큰 값 구하기
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
                
    #print(dp)
    return max(dp[-1])    


#Point
#이전에 풀었던 문제와 비슷

