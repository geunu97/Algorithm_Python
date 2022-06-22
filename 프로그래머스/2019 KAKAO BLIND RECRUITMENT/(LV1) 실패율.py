def solution(N, stages):
    len_value = len(stages)
    result = []
    for i in range(1,N+1):
        count_value = stages.count(i)
        if count_value == 0 or len_value == 0:
            result.append([0, i])
        else:
            result.append( [count_value / len_value, i] )
            
        len_value -= count_value
    
    result = sorted(result, key=lambda x: (-x[0]))
    
    answer = []
    for i in result:
        answer.append(i[1])
    
    return answer

# 1 ~ N까지 각 단계별로 실패율 구하는 문제

#count