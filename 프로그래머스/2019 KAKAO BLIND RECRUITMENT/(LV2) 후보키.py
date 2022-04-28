#LV2 후보키

def solution(relations):
    answer = []
    targets = [[i for i in range(len(relations[0]))]]
    #print(targets)
    
    while targets:
        check = 0
        tmp = targets.pop(0)
        for i in range(len(tmp)):
            list_a = []
            for leng in range(len(relations)):
                a = tmp.copy()
                a.remove(tmp[i])
                b = ''
                for x in a:
                    b += relations[leng][x]
                list_a.append(b)
            if (len(set(list_a)) == len(list_a)) and (a not in targets):
                targets.append(a)
            elif (len(set(list_a)) != len(list_a)):
                check +=1
        if check ==len(tmp):
            answer.append(tmp)
    return len(answer)


#Point
#현재 하나도 이해못함
#다시 이해하기
