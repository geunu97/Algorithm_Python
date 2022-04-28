#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#13. 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 
#    전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하기


N = int(input())
list_a = []
for i in range(N):
    a,b = map(int,input().split())
    list_a.append([a,b])

list_a = sorted(list_a, key = lambda x: x[0])  

dp = [1] * N
for i in range(1,N):
    for j in range(i):
        if list_a[j][0] < list_a[i][0] and list_a[j][1] < list_a[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))


#헐 맞았다....

#Point
#LIS 응용문제