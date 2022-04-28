#11단계: 브루트 포스
#2. 분해합

N = int(input())

finish = 0

for i in range(1,N+1):
    n_1 = i % 10 
    n_10 = i % 100 // 10
    n_100 = i % 1000 // 100
    n_1000 = i % 10000 // 1000
    n_10000 = i % 100000 // 10000
    n_100000 = i % 1000000 // 100000
    n_1000000 = i % 10000000 // 1000000

    if i + n_1 + n_10 + n_100 + n_1000 + n_10000 + n_100000 + n_1000000 == N:
        answer = i
        finish = 1
        break

if finish == 1:
    print(answer)
else:
    print("0")