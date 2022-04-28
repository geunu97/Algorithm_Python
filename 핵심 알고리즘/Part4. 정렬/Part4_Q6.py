#Part4. 정렬
#문제 6. 2019 KAKAO BLIND RECRUITMENT LV1 실패율

def solution(N, stages):

    len_value = len(stages)
    answer1_list = []
    for i in range(1,N+1):
        if len_value == 0:
            fail = 0
        else:
            fail = stages.count(i) / len_value
        
        answer1_list.append([fail,i])
        len_value = len_value - stages.count(i)

    answer1_list = sorted(answer1_list,key = lambda x: (-x[0],x[1]))
        
    answer2_list = []
    for x,y in answer1_list:
        answer2_list.append(y)
    
    return answer2_list


print(solution(4,[4,4,4,4,4]))

