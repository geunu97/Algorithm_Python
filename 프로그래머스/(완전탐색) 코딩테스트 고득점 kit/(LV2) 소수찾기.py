#LV2 소수찾기

from itertools import permutations

#2번째 방법 사용
def sosu(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    list_a = []
    for i in range(1,len(numbers)+1):
        number = list(permutations(numbers,i))
        
        for j in number:
            list_a.append(int("".join(j)))
            
    list_a = list(set(list_a))
    
    answer = 0
    for i in list_a:
        if sosu(i) == True:
            answer += 1

    return answer


#Point
#소수찾기 - 2번째 방법사용 (더 큰 범위까지 가능)
#모든길이 - 조합 - permutations사용