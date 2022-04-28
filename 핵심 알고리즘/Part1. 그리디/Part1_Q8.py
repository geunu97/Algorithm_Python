#Part1. 그리디
#문제 8. 볼링공 고르기 
#        숫자 여러개가 주어졌을 때 두 명이 고를 수 있는 조합의 개수는?  단 서로 숫자가 똑같으면 안된다
# 1 3 2 3 2 
# [1번,2번] [1번,3번] [1번,4번] [1번,5번] [2번,3번] [2번,5번] [3번,4번] [4번,5번]  8개


n,m = map(int,input().split())

list_a = list(map(int,input().split()))

count = 0
for i in range(1,len(list_a)):
  count += i 

min_value = min(list_a)
max_value = max(list_a)

for i in range(min_value,max_value+1):
  if list_a.count(i) > 1:
    value = 0
    for j in range(1,list_a.count(i)):
      value += j
    count = count - value

print(count)

#Point
#전체 갯수(서로 아무것도 겹치는게 없을 때)는 (볼링공 갯수-1 + 볼링공 갯수-2 ... + 1)이 된다.
#가장 작은 수, 가장 큰수를 구해서 -> 가장 작은 수부터 가장 큰 수까지 2개 이상인거 찾기
#2개 이상인거에서도 (해당 값 -1 + 해당 값 -2 ... +1) 계산하기
#전체 갯수에서 바로 위에 계산한 값 빼기


#4+3+2+1 = 10 -2 
#7+6+5+4+3+2+1 = 28 -3 