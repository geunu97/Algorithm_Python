#16단계: 그리디 알고리즘 (탐욕법)
#4. 잃어버린 괄호

   
start = input()

if start[0] == '-':                                  #맨 앞에 수가 -로 시작할 때
    list_a = list(start.split('-'))                  #-를 기준으로 모두 나누기 ( 55 , 50+40 )      
    total = 0
    for i in list_a:                                 
        sum = 0

        for j in i.split('+'):                       #-를 기준으로 나눈 수들을 안에서 한번 더 +로 나눠주기 
            sum += int(j)                            #안에서 다 더한 후 마지막에 -해주기
        total -= sum

else:                                                #맨 앞에 수가 +로 시작할 때
    list_a = list(start.split('-'))                  #-를 기준으로 모두 나누기 ( 55 , 50+40 )
    total = 0
    start = 0
    for i in list_a:
        sum = 0

        if start == 0:                               #맨 앞에 수만 더해주고 시작하기 위해
            for j in i.split('+'):
                sum += int(j)
            total += sum
            start += 1
        
        else:                                        #위에 규칙과 동일
            for j in i.split('+'):
                sum += int(j)
            total -= sum
            
print(total)

#Point
#마이너스 다음 플러스가 있을 때 플러스부터 계산 후 마이너스 붙이기 (ex) -50+40이면 -90)
#a.split('-')  , a.split('+')의 활용이 중요한 문제  

#-로 나누면 -가 없어지면서 -로 나뉨