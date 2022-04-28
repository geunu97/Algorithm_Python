#LV1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    count = 0
    zero_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        else:
            if i in win_nums:
                count += 1
                
    #최고 순위
    answer = []
    if zero_count + count == 6:
        answer.append(1)
    elif zero_count + count == 5:
        answer.append(2)
    elif zero_count + count == 4:
        answer.append(3)
    elif zero_count + count == 3:
        answer.append(4)
    elif zero_count + count == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    #최저 순위
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer



solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])

     