#9단계: 기본 수학 2
#5번 문제

def sosu(i):
    sqrt_num = int(i**0.5)

    for j in range(3,sqrt_num+1,2):          
        if i % j == 0:
            return False
    return True

list_a=[]                  
for x in range(3,123456*2+1,2):
    if sosu(x):
        list_a.append(x)

while True:                              
    a = int(input())

    if a == 1 or a == 2:
        print("1")
        continue
    elif a == 0:
        break

    else: 
        count = 0             # 오래 걸림 !!! 중요!!!!          #리스트안에 하나의 정수가 있나 확인하려면 처음부터 끝까지 비교함, a를 비교했음 
        for i in list_a:      # for i in range(a+1,a*2+1):     #답은 리스트 한번만 돌리면 끝, 리스트 숫자를 돌림!!
            if a<i<=a*2:      #    if i in list_a:    
                count += 1
        print(count)

#리스트 미리 만들기

#짝수면 바로 패스 홀수만 계산, 
#홀수씩 계산, 3~ 제곱근까지 계산
#함수 만들어서 푸는게 쪼금 더 빠름


