#LV3 스티커 모으기
#원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대가 되게 하기
#스티커 한장을 뜯어내면 양쪽으로 인접해 있는 스티커는 찢어져서 사용할 수 없다

def solution(sticker):
    dp=[0] * (len(sticker))
    dp[0] = sticker[0]
    
    dp2 = [0]*len(sticker)
    
    if len(sticker) >= 2:
        dp[1] = max(sticker[0], sticker[1])
        dp2[1] = sticker[1] 
    
    if len(sticker) >= 3:
        for i in range(2,len(sticker)):
            if i == 2:
                dp[i] = max(dp[i-1],dp[i-2]+sticker[i])
                dp2[2] = max(sticker[1], sticker[2])
            
            if i == len(sticker)-1:
                a = max(dp[i-1],dp[i-2])
                b = max(dp2[i-1],dp2[i-2]+sticker[i])
                
                dp[i] = max(a,b)
                
            elif i != len(sticker)-1 and i != 2:   
                dp[i] = max(dp[i-1],dp[i-2]+sticker[i])
                dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])

    return dp[-1]

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))

#Point
#dp문제 & 마지막원소 처리 


#기본 점화식
#max(dp[i-1], dp[i-2] + sticker[i])   2번 연속 금지

#응용
#마지막dp를 구할 때 문제가 되는데 
#1.첫 번째 스티커를 땔 때  2.첫 번째 스티커를 때지 않을 때로 나눌 수 있다
#1번은 첫번째 원소(스티커)를 포함해서 시작하고, 마지막 원소전까지 점하식을 진행하면 된다
#2번은 첫번째 원소(스티커)를 없다고 생각하고 두번쨰 원소부터 마지막 원소까지 점화식을 진행하면 된다

#1번과 2번중 최댓값이 정답이 된다. 
