#LV1 K번째 수

def solution(array, commands):
    
    answer = []
    for i,j,k in commands:
        list_a = []
        for num in array:            #list_a = array이렇게 하면 안됨 // 그냥 list_a가 array를 가리킨다는 뜻 // list_a건들면 array값도 바뀜 // 얕은 복사
            list_a.append(num)       #하나하나 넣어줘야 함 // 2차원 그래프에서도 했던 것 
        
        answer.append(sorted(list_a[i-1:j])[k-1])

    return answer