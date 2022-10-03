n,k = map(int,input().split())
degree = list(map(int,input().split()))

dp = [0] * (n-k+1)
dp[0] = sum(degree[:k])

for i in range(1,len(degree)-k+1):  
  dp[i] = dp[i-1]-degree[i-1]+degree[i+k-1]

print(max(dp))


#dp, 누적합 문제

#단순히 반복문 돌려서 매번 sum으로 더해줘서 비교하면 안됨

#반복문으로 하나씩 이동하면서 가장 왼쪽 수 빼고, 가장 오른쪽 수 더하는 식으로 해야 된다