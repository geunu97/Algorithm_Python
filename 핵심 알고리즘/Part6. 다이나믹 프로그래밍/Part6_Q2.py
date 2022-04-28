#Part6. 다이나믹 프로그래밍(DP)
#문제 2. N개의 식량창고를 입력받아서 식량의 최댓값 구하기 , 인접한 창고는 선택하지 못한다(1칸이상 떨어져 있어야 한다)
# 1 3 1 5의 경우 3과 5 선택 


N = int(input())
list_a = list(map(int,input().split()))

#결과 저장위한 DP테이블
dp = [0] * 100

dp[0] = list_a[0]
dp[1] = max(list_a[0],list_a[1])

for i in range(2,N):  #보텀업 방식
    dp[i] = max(dp[i-1], dp[i-2]+list_a[i])   #중요!


print(dp[N-1])


#Point
#식을 세우기
#2가지로 나눌 수 있음
#n번째의 수를 구하기 위해선
#1) n-1번 선택
#2) n-2번 선택 + n번 선택  
#2개 중에서 최댓값을 구해 나아가면 됨



#안보고 다시 풀어보기


