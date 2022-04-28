#Part6. 다이나믹 프로그래밍(DP)
#문제 5. n*m크기의 금광이 있을 때, 첫번째 열부터 시작하여 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동한다. m번에 걸쳐서 최대 획득 금 구하기

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    list_a = list(map(int,input().split()))

    list_b  = [[0] * M for _ in range(N)]

    k = 0
    for i in range(N):
        for j in range(M):
            list_b[i][j] = list_a[k]
            k += 1
    
    #DP테이블
    dp = [[0] * M for _ in range(N)]

    for i in range(N):
        dp[i][0] = list_b[i][0]

    for j in range(1,M):  #보텀업
        for i in range(N):
            if i == 0:
                dp[i][j] =  max(dp[i][j-1],dp[i+1][j-1]) + list_b[i][j]
            elif i == N-1:
                dp[i][j] =  max(dp[i][j-1],dp[i-1][j-1]) + list_b[i][j]
            else:
                dp[i][j] =  max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1]) + list_b[i][j]

    max_value = -987654321
    for i in range(N):
        for j in range(M):
            max_value = max(max_value,dp[i][j])

    print(max_value)


    #Point
    #1열부터 이전 열의 최댓값을 구하면서 나아가면 됨 
    #처음 행일 때, 마지막 행일 때, 나머지 행일 때로 구별