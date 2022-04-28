#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#4. 파도반 수열

T = int(input())

#DP테이블
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1

for _ in range(T):
    N = int(input())

    for i in range(3,N): #보텀업
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N-1])
    
#파도반 수열 점화식 첫번째, 두번째, 세번째 값 1 , f(x) = f(x-2) + f(x-1)


''''
T = int(input())

#재귀함수 + 딕셔너리 사용
dictionary = {
    1:1,
    2:1,
    3:1
 }

def padoban(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = padoban(n-2) + padoban(n-3)
        return dictionary[n]

for i in range(T):
    n = int(input())

    print(padoban(n))
'''