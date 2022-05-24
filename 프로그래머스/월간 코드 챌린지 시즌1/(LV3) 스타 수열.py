#LV3 스타 수열

from collections import Counter

def solution(a):
    answer = -1
    dic = Counter(a)
    
    for i in dic:
        if dic[i] <= answer:
            continue
            
        i_count = 0   
        index = 0
        while index < len(a)-1:
            if (a[index] == i or a[index+1] == i) and (a[index] != a[index+1]):
                i_count += 1   #i 사용횟수 1증가
                index += 2          #인덱스 2 점프
            else:
                index += 1          #바로 다음 인덱스
            
        answer = max(i_count, answer) 
    
    
    return answer * 2
    
    
    
    #1. 배열a에 사용된 숫자 반복문 돌리기 (Counter를 사용해서 해당 숫자가 몇번 등장 했는지 딕셔너리 형태로 변환)
    #   -해당 숫자를 공통된 숫자로 정의하기

    #2. 배열 a를 처음부터 끝까지 돌면서, 공통된 숫자가 포함됐는지 등 조건 따지기
    #   -조건이 성립한다면, 공통된 숫자 사용횟수 +1 와 인덱스 2번 점프하기
    #   -조건이 X라면, 바로 다음 인덱로 넘어가기
        
    #3. 마지막에, 공통된 숫자 사용횟수와 기존 답 중에서 최댓값 저장하기
    
    #4. dic[i] <= answer 조건을 통해, 해당 숫자의 갯수가 답으로 구한 숫자의 갯수보다 작다면 미리 넘어가도록 할 수 있다
    #   -당연히 해당 숫자의 갯수가 많아야, 답으로 구할 숫자의 갯수가 더 많아질 수 있기 때문
    
    #5. 최종 답으로 구한 공통된 숫자의 사용 횟수 * 2해주면 스타 수열의 길이를 구할 수 있다 
