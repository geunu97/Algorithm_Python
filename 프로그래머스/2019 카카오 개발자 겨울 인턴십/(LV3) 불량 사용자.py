from itertools import permutations

def solution(user_id, banned_id):
    combi = list(permutations(user_id, len(banned_id)))
    
    answer = []
    for com in combi:
        result = []
            
        for i in range(len(com)):
            if len(com[i]) == len(banned_id[i]):
                check = 1
                for j in range(len(com[i])):
                    if banned_id[i][j] == '*':
                        continue
                    if com[i][j] != banned_id[i][j]:
                        check = 0
                        break

                if check == 1:
                    result.append(com[i])
        
        if len(result) == len(banned_id) and sorted(result) not in answer:
            answer.append(sorted(result))
    
    
    
    return len(answer)



# 오래 걸렸던 문제

# 다시 보기!!!