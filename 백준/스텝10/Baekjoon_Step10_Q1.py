#10단계: 재귀
#1. 팩토리얼

def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        return a * factorial(a-1)

a = int(input())

print(factorial(a))