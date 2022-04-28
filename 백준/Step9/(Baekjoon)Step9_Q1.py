#9단계: 기본 수학 2
#1. 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

a = int(input())

list_a = list(map(int,input().split()))

count = 0

for i in range(a):
    no_count = 0

    if list_a[i] == 1:
        continue

    elif list_a[i] == 2:
        count += 1
        continue

    else:
        for j in range(2,list_a[i]):
            if list_a[i] % j == 0:
                no_count = 1
                break

    if no_count != 1:
        count += 1

print(count)

# 주어진 수 % i (2 ~ n-1까지 반복문 돌린 수) == 0 이면 아님