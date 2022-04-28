#LV2 튜플

def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    
    list_a = []
    for i in s:
        i = i.split(',')    #이렇게 안하면 111이 나눠짐
        list_b = [len(i)]
        
        for j in i:
            list_b.append(j)
    
        list_a.append(list_b)

    list_a = sorted(list_a,key=lambda x: x[0])
    
    answer = []
    for i in list_a:
        for j in range(1,len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
  
    #print(answer)
    return answer


#Point
#split() 응용문제

#입력이 문자열형태로 기호들과 함께 주어지는 경우    ->   s = s[2:-2]
#split으로 분리하기 , 그 안에서 또 split으로 분리하기

#그 다음엔 길이순으로 정렬해서 없는 수 하나씩 넣으면 됨