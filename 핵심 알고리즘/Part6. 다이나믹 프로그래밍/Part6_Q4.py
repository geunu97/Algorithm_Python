#Part6. 다이나믹 프로그래밍(DP)
#문제 4. N가지 종류의 화폐가 있을 때 최소의 갯수를 사용해서 M원 만들기


N,M = map(int,input().split())
list_a= []
for i in range(N): 
    list_a.append(int(input()))

#DP테이블
dp = [10001] * (M+1)

dp[0] = 0   
for i in list_a:  #보텀업
    for j in range(i, M+1):
        dp[j] = min(dp[j], dp[j - i] + 1)


if dp[M] == 10001:
    print('-1')
else:
    print(dp[M])


#Point
#이전 그리디 문제에서와 비슷한 문제지만 큰 동전이 작은 동전의 배수가 아니라는 점이 차이다

#단위 하나씩 차례대로 모두 확인 (2일때, 3일때 ... )
#2일 때 M까지 확인 -> a(2) = a(0) + 1 // a(3) = a(1) + 1 // a(4) = a(2) + 1  ...
#3일 때 M까지 확인 -> a(3) = a(0) + 1 // a(4) = a(1) + 1 // a(5) = a(2) + 1  ...
#4일 때 M까지 확인 -> a(4) = a(0) + 1 // a(5) = a(1) + 1 // a(6) = a(2) + 1  ...

#기존에 넣어뒀던 값과 비교해서 최솟값 넣기

