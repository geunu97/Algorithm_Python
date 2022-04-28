#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#16. (DP의 대표적인 문제 : 0-1 냅색 문제 : 주어진 용량을 초과하지 않으면서 전체 이득이 최대가 될 수 있도록 하는 문제) 배낭 문제
#    용량이 정해진 배낭 가방과 가치와 무게가 다른 다른 여러 개의 물건들이 주어졌을 때 용량을 초과하지 않으면서 전체 가치의 합이 최대가 되도록 구하는 문제


N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0]*(K+1) for _ in range(N+1)]   #2차원 DP테이블

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):   #i는 행
    for j in range(1, K + 1):   #j는 열(=최대 무게)
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])