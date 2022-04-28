#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#5. 빨강,초록,파랑 3가지 색을 N개의 줄에 각 행마다 3개씩 집이 있을 때 집에 색칠을 하려고 한다
#   (조건은 1번과 2번의 집의 색이 같지 않으며, N번 집의 색과 N-1번 집의 색이 같지 않아야 하며 i-1번, i+1번 집의 색과 같지 않아야 한다.)

n = int(input())

dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))  #DP테이블

for i in range(1,n):  #보텁업                                 
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])                
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])                
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])               

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))             #마지막 줄에서 최소값 구하기
