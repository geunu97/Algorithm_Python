#LV2 k진수에서 소수 개수 구하기

#소수판별 2번째 방법
def check_(number):
    if number == 1:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    
    return True

#n을 k진법으로 변환 (노트에 써놓기)
def change(num,k):
    result = []
    while True:
        result.append(num % k)
        num = num // k
        
        if num == 0:
            break
    
    result.reverse()
    return result

def solution(n, k):
    change_k_list = change(n,k)  #k진법으로 변환
    change_k_str = ""
    for i in change_k_list:   #split사용하기 위해 리스트를 문자열로 변환
        change_k_str += str(i)
    
    list_a = change_k_str.split('0')    #0으로 구분하기
    
    #print(list_a)
    
    answer = 0
    for i in list_a:
        if len(i) >= 1:
            if check_(int(i)) == True:     #소수 판별하기
                answer += 1
    
    return answer



#Point
#n을 k진법으로 바꾼뒤 -> 0으로 구분해서 각 수를 소수판별하면 된다 -> 이때 각 수를 10진수로 보기때문에 자리수가 많이 늘어나게 된다 -> 
# 따라서 범위가 한정되어있는 에라토스테네스의 체보다 2번째 방법을 사용하여 소수판별하는 것이 더 큰 범위까지 판별할 수 있다 


'''
#소수리스트, 에라토스테네스의 체     #사용시 런타임에러
sosu_list = [True] * 1000001
sosu_list[0] = False
sosu_list[1] = False
for i in range(2,1000001):
    if sosu_list[i]:
        for j in range(i*2, 1000001, i):
            sosu_list[j] = False
'''