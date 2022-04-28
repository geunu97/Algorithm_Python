#LV1 부족한 금액 계산하기

def solution(price, money, count):
    
    cnt = 1
    sum = 0
    while True:
        sum += (price * cnt)
        cnt += 1
        
        if cnt == count+1:
            break
    
    if sum <= money:
        return 0
    else:
        return sum-money

