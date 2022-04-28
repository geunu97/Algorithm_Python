#12단계: 정렬
#4. 통계학 (최빈값 풀어내는 법 + 평균,중앙값,최대-최소 범위)

from collections import Counter        #collections 모듈의 Counter 클래스   (from 모듈이름 import 모듈에서 가져올 함수(변수) 이름)
                                       #문자열이나 리스트에서 어떤 객체가 몇 번 등장했는지 계산해서 딕셔너리로 만들어줌
import sys
input = sys.stdin.readline             #빠르게 입력받기

N = int(input())

list_a=[]
for i in range(N):
    list_a.append(int(input()))

answer1 = sum(list_a) / N

answer2_list = sorted(list_a)
answer2 = answer2_list[N//2]

counter_dic = Counter(answer2_list)   #중복되는 것에 개수를 세서 딕셔너리로 만들어줌 Counter()   , 미리 정렬되어 있는 리스트로 활용
counter_list = counter_dic.most_common()  #빈도가 큰 순서대로 정렬해서 리스트 튜플 형태로 만들어줌 .most_common() 
if len(counter_list) == 1:   #튜플 하나당 길이 1
    answer3 = counter_list[0][0]    #해당 튜플 인덱스에 접근하는 법
else:
    if counter_list[0][1] == counter_list[1][1]:
        answer3 = counter_list[1][0]
    else:
        answer3 = counter_list[0][0]

min = min(list_a)
max = max(list_a)
answer4 = max - min
    
print(round(answer1))   #round() 반올림 내장함수 사용 
print(answer2)
print(answer3)
print(answer4)
