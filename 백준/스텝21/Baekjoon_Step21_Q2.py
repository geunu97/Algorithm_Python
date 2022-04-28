#15단계: 이분 탐색(이진 탐색)
#2. 리스트 2개를 입력받아 하나의 리스트 안에 값들 각각 다른 리스트에 몇개 있는지 구하기

from bisect import bisect_left, bisect_right

N = int(input())
list_a = list(map(int,input().split()))

M = int(input())
list_b = list(map(int,input().split()))

list_a = sorted(list_a)   #반드시 정렬된 상태로 시작

def count_by_range(left_value,right_value):
    left_index = bisect_left(list_a,left_value)
    right_index = bisect_right(list_a,right_value)
    
    return right_index - left_index


answer = []
for i in list_b:
    answer.append(count_by_range(i,i))

for i in answer:
    print(i,end= " ")


#정답 ~.~