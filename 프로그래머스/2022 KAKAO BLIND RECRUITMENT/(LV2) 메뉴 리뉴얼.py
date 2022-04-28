#LV2 메뉴 리뉴얼

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        list_a = []
        for order in orders:
            combi = combinations(sorted(order), c)   #AB와 BA를 같게처리해야 하기 떄문에 정렬
            list_a += combi
            
        counter = Counter(list_a)
        #print(counter)    
        if len(counter) != 0 and max(counter.values()) != 1:
            for i in counter:
                if counter[i] == max(counter.values()):   #가장 많이 사용된 것을 찾는것임
                    answer.append(''.join(i))
                    
            
    return sorted(answer)


#Point
#course의 각각 갯수만큼 조합을 구하는 문제 (2개짜리 조합, 3개짜리조합 ...)
#문제를 잘못 이해했던게 만약 2개짜리 조합들을 구한다고 했을 때
#이 중에서 2번이상 사용됐으며, 가장 많이 사용된 갯수만큼 사용된 조합을 찾아야함 !!!!!


#itertools - combinations 사용
#collections - Counter 사용


#Counter부분 파이썬노트 Counter모듈부분에 써놓기
