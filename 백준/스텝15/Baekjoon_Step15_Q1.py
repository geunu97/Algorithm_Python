#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#1. 피보나치 함수, N이 주어졌을 때 f(0)과 f(1)이 각각 몇 번 출력되는지 구하기

T = int(input())

def fibo(i):
    DP.append([DP[i-2][0] + DP[i-1][0], DP[i-2][1] + DP[i-1][1]])

for _ in range(T):
    DP=[[1,0],[0,1]]   #DP테이블   #0일때, 1일때 미리 넣어놓기

    a = int(input())

    if a != 0 or a != 1:
        for x in range(2,a+1):  
            fibo(x)

    print(DP[a][0],DP[a][1])



#단지 피보나치 규칙에서 0과1이 몇번 들어갈지 알아보기 위한 문제

