#3단계: for문
#11. 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

a,b = map(int,input().split())
list_a = list(map(int, input().split()))

for i in range(a):
    if list_a[i] < b:
        print(list_a[i], end=" ")