#9단계: 기본 수학 2
#3. 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

a = int(input())

i = 1

while True:
    i += 1

    if a % i == 0:
        print(i)
        a = a // i
        i = 1

    elif a == 1:
        break