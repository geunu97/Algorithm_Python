#12단계: 정렬
#1. 수 정렬하기

n = int(input())

list_a=[]
for i in range(n):
    list_a.append(int(input()))

answer_list = sorted(list_a)          #sorted 함수 사용!!

for j in range(len(answer_list)):
    print(answer_list[j])

