#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#9. 인접한 모든 자리의 차이가 1인 수를 계단 수라고 한다. 0으로 시작하는 수는 계단수가 아니다. (ex) 45656 )
#   N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하기


N = int(input())

#DP테이블
dp = [1] * 10
dp[0] = 0     #초기값(길이1)   

for _ in range(1,N):
    new = [0] * 10
    for i in range(10):
        if i == 0:
            new[1] += dp[i]
        elif i == 9:
            new[8] += dp[i] 
        else:
            new[i-1] += dp[i]
            new[i+1] += dp[i]
    dp = new

print(int(sum(dp) % 1000000000))

#Point
#끝자리가 0일때, 9일 때, 나머지로 나누어서 갯수 더해주면서 나아가기
