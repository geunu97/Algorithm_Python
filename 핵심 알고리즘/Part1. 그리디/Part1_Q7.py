#Part1. 그리디
#문제 7.  여러개의 동전을 받아서 만들 수 없는 최소 금액을 구해라 (1부터)
# 5
# 3 2 1 1 9
# 답 : 8

n = int(input())
list_a = list(map(int,input().split()))

list_a = sorted(list_a)   #정렬 해야됨 => 그리디

target = 1
for x in list_a:
  if target < x:
    break
  target += x

print(target)


'''
#sum_list에 자기자신 포함 모든 합계 넣기
sum_list=[]
for i in range(len(list_a)-1):
  for j in range(i+1,len(list_a)):
    j = j+1
    sum_value = sum(list_a[i:j])          #인덱싱 사용   #딱 숫자 2개만 고르는게 아니라 범위를 사용해야되기 때문에!!!
    sum_list.append(sum_value)

for j in list_a:
  sum_list.append(j)                       

sum_list = list(set(sum_list))            #중복제거   #set()함수 list()로 꼭 감싸주기

for i in range(1,max(list_a)):            #1부터 없는 수 구하기
  if i not in sum_list:
    print(i)
    break
'''