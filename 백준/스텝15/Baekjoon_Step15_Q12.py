#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#12. 바이토닉 수열, Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
#    예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이다
#    부분 수열 중 가장 긴 바이토닉 수열의 길이 구하기


N = int(input())
list_a = list(map(int,input().split()))
reverse_list_a = list_a[::-1]  #뒤집기

increase_dp = [1] * N   #증가하는 수열 DP테이블
decrease_dp = [1] * N   #감소하는 수열 DP테이블

for i in range(1,N):
    for j in range(i):
        #증가하는 수열
        if list_a[j] < list_a[i]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

        #감소하는 수열 (리스트 뒤집어서 증가하는 수열처럼 계산하기)
        if reverse_list_a[j] < reverse_list_a[i]:   
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

#결과값 넣어주기
result = [1] * N 
for i in range(N): 
    result[i] = increase_dp[i] + decrease_dp[N-i-1] -1   #겹치는 부분때문에 -1

print(max(result))


#Point
#LIS 응용문제

#증가 dp, 감소 dp 테이블 2개 만들기 + 결과 테이블 1개 만들기


