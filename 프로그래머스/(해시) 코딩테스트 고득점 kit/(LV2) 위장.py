#LV2 위장

def solution(clothes):
    dictionary = {}
    for i in clothes:
        if i[1] not in dictionary:
            dictionary[i[1]] = [i[0]]
        else:
            dictionary[i[1]].append(i[0])
    
    #print(dictionary)
    
    answer = 1
    for key in dictionary:
        answer *= len(dictionary[key])+1          # +1해주는 이유는 아무것도 선택하지 않았을 때도 포함하기 때문
    
    return answer-1     # 마지막에 -1해주는 이유는 뭐든 적어도 1개는 입어야 하기 때문


#Point
#조합의 개수 구하는 문제 (단, 같은 종류는 1개만 가능)