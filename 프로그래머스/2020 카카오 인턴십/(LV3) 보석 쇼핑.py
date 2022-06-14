def solution(gems):
    dictionary = {
        gems[0]: 1
    }
    
    left_index = 0
    right_index = 0
    
    ans_left_index = -987654321
    ans_right_index = 987654321
    
    kind_gems_len = len(list(set(gems)))
    gems_len = len(gems)
    
    while True:
        if left_index == gems_len or right_index == gems_len:
            break
            
            
        if len(dictionary) < kind_gems_len:
            right_index += 1
            if right_index == gems_len:
                break
            
            if gems[right_index] in dictionary:
                dictionary[gems[right_index]] += 1
            else:
                dictionary[gems[right_index]] = 1
        
        
        elif len(dictionary) == kind_gems_len:
            if (right_index - left_index)  <  (ans_right_index - ans_left_index):
                ans_left_index = left_index
                ans_right_index = right_index
        
            
            if dictionary[gems[left_index]] == 1:
                del dictionary[gems[left_index]]
            else:
                dictionary[gems[left_index]] -= 1
            
            left_index += 1
            
                
    return [ans_left_index+1,ans_right_index+1]
    

#투 포인터 

#범위의 시작 => 왼쪽 인덱스
#범위의 끝 -> 오른쪽 인덱스