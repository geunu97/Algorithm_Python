#10단계: 재귀
#2. 피보나치 수 5


#방법1: 메모이제이션
'''
dictionary = {
    1:1,
    2:1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        dictionary[n] = fibonacci(n-1) + fibonacci(n-2)
        return dictionary[n]

n = int(input())

print(fibonacci(n))
'''

#방법2: 단순 재귀사용 
'''
def fibo(a):
    if a == 0:
        return 0

    elif a == 1 or a == 2:
        return 1

    else:
        return fibo(a-1) + fibo(a-2)

a = int(input())

print(fibo(a))
'''