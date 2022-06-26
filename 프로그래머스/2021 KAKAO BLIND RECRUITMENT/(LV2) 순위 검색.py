#LV2 순위 검색

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    dictionary = {}
    for i in info:
        i = i.split(' ')
        for j in range(5):
            combi = list(combinations(i[:4],j))
            for com in combi:
                str_value = " ".join(list(com))
                if str_value in dictionary:
                    dictionary[str_value].append(int(i[4]))
                else:
                    dictionary[str_value] = [int(i[4])]
    
    for key in dictionary:
        dictionary[key].sort()
    
    answer = []
    for q in query:
        q = q.split(' and ')
        value = q[3].split(' ')
        q[3] = value[0]
        
        str_value = []
        for i in q:
            if i != '-':
                str_value.append(i)
        str_value = " ".join(str_value)
        
        if str_value in dictionary:
            result = dictionary[str_value]
            answer.append(len(result) - bisect_left(result, int(value[1])))
        else:
            answer.append(0)
            
    
    return answer