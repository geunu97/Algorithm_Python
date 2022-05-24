#LV3 스타 수열

from collections import Counter

def solution(a):
    #print(Counter(a))
    
    max_value = Counter(a).most_common(1)[0][0]
    #print(max_value)
    
    answer = 0
    for i in range(0,len(a)-1,2):
        if (a[i] == max_value or a[i+1] == max_value) and (a[i] != a[i+1]):
            answer += 2
    
    print(answer)
    return answer
    

        

        
#각 배열에 해당 원소가 몇번 등장했는지가 중요하다. 많이 등장할수록 스타 수열의 길이가 길어질 수도 있기 때문에

#Counter: 몇 번 등장했는지 구해서, 딕셔너리 형태로 반환된다
