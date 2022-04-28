#Part6. 다이나믹 프로그래밍(DP)
#문제 7. 병사 선택하기, 병사를 전투력이 내림차순으로 되게 선택할 때 병사의 수가 최대가 되도록 열외시키는 병사의 수 구하기

# 병사번호   1 2 3 4 5 6 7           
# 전투력    15 11 4 8 5 2 4       ->    15 11 8 5 4  (5)     ->    7 - 5 = 2


N = int(input())
list_a = list(map(int,input().split()))

list_a.reverse()

#DP테이블
dp = [1] * N

for i in range(1,N):
    for j in range(0,i):
        if list_a[j] < list_a[i]:
            dp[i] = max(dp[i], dp[j] + 1)


print(N - max(dp))


#Point
#LIS 문제와 매우 비슷한 문제, 따라서 내림차순이 아니라 오름차순으로 풀기 위해 리스트 뒤집기

#1. DP테이블 1로 모두 초기화 시키기
#2. 인덱스 1부터 인덱스 마지막까지 차레대로 마지막 원소 되기
#3. 왼쪽수들과 마지막원소 비교 // 왼쪽 수보다 마지막 원소가 클 때 dp[i] = max(dp[i], dp[j] + 1)     