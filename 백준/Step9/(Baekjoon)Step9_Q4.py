#9단계: 기본 수학 2
#4. M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

m,n = map(int,input().split())

def sosu(i):
    sqrt_num = int(i**0.5)

    for j in range(3,sqrt_num+1,2):     #약수는 대칭성이 있어서 절반만 확인하면 소수인지 확인가능
        if i % j == 0:
            return False
    return True

for i in range(m,n+1):
    if i == 1:
        continue
    elif i == 2:
        print(i)
        continue
    elif i % 2 == 0:
        continue
    else:
        if sosu(i):
            print(i)

        # 짝수는 바로 넘어가기, 홀수 중에서만 계산하기 
        # 2부터 int(제곱근+1) 까지 반복문 돌려서 반복문 돌린 수 i 가 주어진 홀수와 계산하면 됨
        # 주어진 홀수 % i == 0 이면 소수 아님
        # 함수를 사용하면 조금 더 빠르게 계산할 수 있음

        # 더 빠른 방법 존재