def solution(number, k):
    stack = []
    count = 0
    
    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
        
        else:     
            while len(stack) > 0:
                if stack[-1] < number[i]:
                    stack.pop()
                    count += 1
                    
                    if count == k:   #????? 여기 조건식 있어야 성공함
                        stack.append(number[i:])
                        return ''.join(stack)
                else:                    
                    break
                    
            stack.append(number[i])
 
    
    if count < k:         #예외  #k만큼 제거 안했는데 오름차순으로 되어 있을 때  #4 2 1
        return ''.join(stack[:-(k-count)])


#스택 문제

#연속된 숫자 중 앞에서 오는 게 더 크면 된다