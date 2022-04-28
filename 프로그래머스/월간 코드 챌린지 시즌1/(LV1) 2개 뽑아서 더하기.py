#LV1 2개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer =[]
    number_list = list(combinations(numbers,2))

    for i in number_list:
        sum = 0
        for number in i:
            sum += number
        answer.append(sum)
        
    answer = list(set(answer))
    answer = sorted(answer)
    return answer