#5단계: 1차원 배열
#1. N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

a = int(input())
list_a=list(map(int,input().split()))
min = 1000000
max = -1000000

for i in range(a):
    if list_a[i] <= min:
        min = list_a[i]
    if list_a[i] >= max:
        max = list_a[i]

print(min,max)

