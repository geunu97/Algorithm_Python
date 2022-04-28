#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#11. (LIS) 가장 긴 증가하는 부분 수열 최대 길이 구하기


N = int(input())
list_a = list(map(int,input().split()))

dp = [1] * N
for i in range(1,N):    #원소 하나씩 모두 보기
    for j in range(i):   #왼쪽에 있는 원소들과 비교 
        if list_a[j] < list_a[i] :  #가장 오른쪽 원소가 크다면
            dp[i] = max(dp[i], dp[j] + 1) #핵심

print(max(dp))  #dp[N-1]이 아니라 max(dp)


#Point
#이전 병사 전투력 문제와 같은 문제