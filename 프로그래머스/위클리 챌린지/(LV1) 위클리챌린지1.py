#LV1 최소직사각형 
#가로 세로의 길이가 주어지며 가장 작게 명함 케이스를 만드는 문제 (명함을 돌려서 넣을 수도 있다)

def solution(sizes):
    list_a=[]
    list_b=[]
    
    for a,b in sizes:
        if a > b:   #가로 세로 비교
            list_a.append(a)
            list_b.append(b)
        else:
            list_a.append(b)
            list_b.append(a)
            
    value1 = max(list_a)
    value2 = max(list_b)
    
    return value1 * value2


#Point
#하나의 명함당 가로 세로 중에서 큰 값을 list_a, 작은 값을 list_b에 넣고
#list_a에서 최댓값, list_b에서 최댓값 찾으면 된다