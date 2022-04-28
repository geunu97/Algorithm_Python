#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#10. 일렬로 놓여있는 N개의 포도주 잔과 각 잔에는 포도주의 양이 주어질 때 최대로 마실 수 있는 양은?
#    (조건은 1.연속으로 놓여 있는 3잔을 모두 마실 수는 없다)

N = int(input())
list_a = []
for _ in range(N):
    list_a.append(int(input()))

#DP테이블
dp = [0] * N
dp[0] = list_a[0]

if N >= 2:
    dp[1] = list_a[0] + list_a[1]
if N >= 3:
    for i in range(2,N): #보텀업  #3부터 하면 틀림... 
        dp[i] = max(dp[i-2]+list_a[i], dp[i-3]+list_a[i-1]+list_a[i], dp[i-1])  #핵심 

print(dp[N-1])


#Point
#이전 계단 오르기 문제와 3연속X로 비슷하지만 이번 문제는 마지막은 꼭 밟을 필요가 없다 

#따라서 식이 3가지가 나온다  
#N-1               #이전 잔만
#N-2 + N           #전전 잔 + 마지막 잔
#N-3 + N-1 + N     #전전전 잔 + 전 잔 + 마지막 잔

#중에서 최댓값 선택하면 됨


