#LV2 이진 변환 반복하기

def solution(s):
    zero = s.count('0')
    one = '1' * (len(s) - zero)
    one = str("{:b}".format(len(one)))
    
    if one == '1':
        return [1,zero]
    
    count = 1
    while True:
        count += 1
        
        zero_count = one.count('0')
        zero += zero_count

        one = '1' * (len(one) - zero_count)
        one = str("{:b}".format(len(one)))

        if one == '1':
            return [count,zero]
 
    
print(solution("0111010"))
