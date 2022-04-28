#9단계: 기본 수학 2
#6번 문제

# 더더 빠른 에라토스테네스의 체 (2의 배수 지우고, 3의 배수 지우고, 5의 배수 지우고, 첫 수는 소수 , ...)
import sys
input = sys.stdin.readline      #더 빠르게 입력받기

list_sosu = []
for x in range(10001):  
    list_sosu.append(True)       # 리스트 내포 표현 sosu = [True for _ in range(10001)]

list_sosu[0] = False
list_sosu[1] = False

for i in range(2, 101):
    if list_sosu[i]:
        for j in range(i*2, 10001, i):
            list_sosu[j] = False

a = int(input())

for k in range(a):
    num = int(input())
    for i in range(num//2, 10001):
        if list_sosu[i] and list_sosu[num-i]:
            print(num-i, i)
            break



'''
import sys
input = sys.stdin.readline

a = int(input())

for i in range(a):
    b = int(input())

    for j in range(b//2,b+1):   # 주어진 수/2 부터 하나의 값만 먼저 구하기 
        finish = 0

        sqrt_num = int(j**0.5)
        for k in range(2,sqrt_num+1):
            if j % k == 0:
                finish = 1
                break
        if finish != 1:
            number_2 = j
            number_1 = b - j
            ffinish = 0

            sqrt_num = int(number_1**0.5)
            for k in range(2,sqrt_num+1):
                if number_1 % k == 0:
                    ffinish = 1
                    break

            if ffinish != 1:
                print(number_1,number_2)
                break
'''