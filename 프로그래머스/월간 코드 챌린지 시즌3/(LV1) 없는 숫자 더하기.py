#LV1 없는 숫자 더하기

def solution(numbers):
    list_a = [1] * 10
    for i in numbers:
        list_a[i] -= 1
    
    answer = 0
    for index in range(10):
        if list_a[index] == 1:
            answer += index
            
    return answer