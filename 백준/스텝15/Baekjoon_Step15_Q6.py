#15단계: 동적 계획법1 (dp 다이나믹프로그래밍)
#6. 정수삼각형 (꼭대기에서부터 바닥까지 내려오는데 최대합 경로 구하기)

n = int(input())

dp = []
for i in range(n):
    list_a = list(map(int,input().split()))
    dp.append(list_a)    #DP테이블

for i in range(1,n):  #보텀업
    dp[i][0] += dp[i-1][0]    #가장 왼쪽에 있는 수 그냥 더해주기
    dp[i][-1] += dp[i-1][-1]  #가장 오른쪽에 있는 수 그냥 더해주기

    if i >= 2:    #가운데 있는 수
        for j in range(1,i):
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])   

print(max(dp[n-1])) #마지막 줄에서 최댓값 찾기



#Point 
#가장 왼쪽에 있는 수, 가장 오른쪽에 있는 수, 가운데 있는 수들로 나눠야 됨