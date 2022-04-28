#LV1 3진법 뒤집기

def solution(n):
    answer = ""
    while True:
        if n <= 2:
            answer += str(n)
            break
        
        answer += str(n % 3)
        n = n // 3
        
    return int(answer,3)

print("{:b}".format(int(2)))