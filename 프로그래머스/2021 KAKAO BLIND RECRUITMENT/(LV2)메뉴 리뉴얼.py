#LV2 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
    dictionary = {}
    for order in orders:
        for i in course:
            if len(order) >= i:
                combi = list(combinations(sorted(order), i))
                for com in combi:
                    if "".join(com) in dictionary:
                        dictionary["".join(com)] += 1
                    else:
                        dictionary["".join(com)] = 1
    
    answer = []
    for i in course:
        max_value = 1
        result = []
        for key in dictionary:
            if i == len(key):
                if max_value > 1 and max_value == dictionary[key]:
                    result.append(key)
                elif max_value < dictionary[key]:
                    result = [key]
                    max_value = dictionary[key]
                    
        if max_value != 1:
            for res in result:
                answer.append(res)
                
    return sorted(answer)