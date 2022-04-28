#15단계: 동적 계획법1 (stairs 다이나믹프로그래밍)
#7. 계단 오르기, 바닥에서부터 시작해 도착점까지 계단을 밟아 점수를 획득하여 올라야 한다. 얻을 수 있는 총 점수의 최댓값 구하기
#    조건은 1.계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
#           2.연속된 세 개의 계단을 모두 밟아서는 안 된다. 시작점은 계단에 포함하지 않는다
#           3.마지막 도착 계단은 반드시 밟아야 한다 

N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))

#DP테이블 
dp = [0] * 301 

dp[0] = stairs[0]

if N >= 2:
    dp[1] = stairs[0] + stairs[1]
if N >= 3:
    dp[2] = max(stairs[0] , stairs[1]) + stairs[2]
if N >= 4:
    for i in range(3,N):  #보텀업
        dp[i] = max(dp[i-2] , dp[i-3] + stairs[i-1]) + stairs[i]      #핵심!  #(이전 합들 dp[i-2] , 이전합 dp[i-3] + 현재 계단 stairs[i-1] 과 비교해야됨) 
 
print(dp[N-1])


#식세우기
#마지막을 반드시 밟아야할 때 경우의 수 2가지 (N-2, N-1)
#N-2 
#N-1 -> 3개 연속 밟을 수 없으니 -> N-3 + N-1 
#둘 중에 최댓값
 
'''
- 마지막 계단은 무조건 밟아야 하므로, 다음과 같이 두 경우로 나눌 수 있다.

   1) 마지막 계단의 전 계단을 밟음.
   2) 마지막 계단의 전전 계단을 밟음.

- 1)의 경우, 연속된 계단 3개를 밟을 수 없으므로, 마지막 계단의 전전계단은 밟을 수 없다. 그러므로 마지막 계단의 전전전 계단을 밟은 것이다.
- 이를 식으로 나타낼 경우 다음과 같다.
   1) sum[n] = sum[n-3] + stair[n-1] + stair[n]
   2) sum[n] = sum[n-2] + stair[n]
- 위 두 값 중 큰 값을 선택하여 최댓값을 구할 수 있다.
'''