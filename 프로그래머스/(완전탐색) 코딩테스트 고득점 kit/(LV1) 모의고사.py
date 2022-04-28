#LV1 모의고사

def solution(answers):
    list_a = [1,2,3,4,5]
    list_b = [2,1,2,3,2,4,2,5]
    list_c = [3,3,1,1,2,2,4,4,5,5]
    
    a = 0
    b = 0
    c = 0
    for i in range(len(answers)):
        index = i % len(list_a)      
        if list_a[index] == answers[i]:
            a += 1
        print(index)
            
        index = i % len(list_b)
        if list_b[index] == answers[i]:
            b += 1 
            
        index = i % len(list_c)
        if list_c[index] == answers[i]:
            c += 1
    
    
    result = []
    answer = max(a,b,c)
    if answer == a:
        result.append(1)
    if answer == b:
        result.append(2)
    if answer == c:
        result.append(3)
    
    result = sorted(result)
    return result


#Point
#원형 모양일 때도 마찬가지로 범위가 벗어날 때 %를 사용하거나 // 응용 문제(길이가 한바퀴 돌때마다 달라질 때)는 % // + 사용할 수도 있다

