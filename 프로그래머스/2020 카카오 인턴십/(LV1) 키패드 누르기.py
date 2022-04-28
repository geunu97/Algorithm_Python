#LV1 키패드 누르기

def solution(numbers, hand):
    answer = ""
    left = [3,0]
    right = [3,2]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            if i == 1:
                left = [0,0]
            elif i == 4:
                left = [1,0]
            elif i == 7:
                left = [2,0]
                
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            if i == 3:
                right = [0,2]
            elif i == 6:
                right = [1,2]
            elif i == 9:
                right = [2,2]           
            
        else:
            if i == 2:
                if abs(left[0] - 0) + abs(left[1] - 1) == abs(right[0] - 0) + abs(right[1] - 1):
                    if hand[0].upper() == 'R':
                        answer += 'R'
                        right = [0,1]
                    else:
                        answer += 'L'
                        left = [0,1]
                elif abs(left[0] - 0) + abs(left[1] - 1) < abs(right[0] - 0) + abs(right[1] - 1):
                    answer += 'L'
                    left = [0,1]
                else:
                    answer += 'R'
                    right = [0,1]
            elif i == 5:
                if abs(left[0] - 1) + abs(left[1] - 1) == abs(right[0] - 1) + abs(right[1] - 1):
                    if hand[0].upper() == 'R':
                        answer += 'R'
                        right = [1,1]
                    else:
                        answer += 'L'
                        left = [1,1]
                elif abs(left[0] - 1) + abs(left[1] - 1) < abs(right[0] - 1) + abs(right[1] - 1):
                    answer += 'L'
                    left = [1,1]
                else:
                    answer += 'R'
                    right = [1,1]
            elif i == 8:
                if abs(left[0] - 2) + abs(left[1] - 1) == abs(right[0] - 2) + abs(right[1] - 1):
                    if hand[0].upper() == 'R':
                        answer += 'R'
                        right = [2,1]
                    else:
                        answer += 'L'
                        left = [2,1]           
                elif abs(left[0] - 2) + abs(left[1] - 1) < abs(right[0] - 2) + abs(right[1] - 1):
                    answer += 'L'
                    left = [2,1]
                else:
                    answer += 'R'
                    right = [2,1]
            elif i == 0:
                if abs(left[0] - 3) + abs(left[1] - 1) == abs(right[0] - 3) + abs(right[1] - 1):
                    if hand[0].upper() == 'R':
                        answer += 'R'
                        right = [3,1]
                    else:
                        answer += 'L'
                        left = [3,1]                
                elif abs(left[0] - 3) + abs(left[1] - 1) < abs(right[0] - 3) + abs(right[1] - 1):
                    answer += 'L'
                    left = [3,1]
                else:
                    answer += 'R'
                    right = [3,1]
                    
    return answer