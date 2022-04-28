#Part4. 정렬
#문제 1. 내림차순으로 정렬하기

N = int(input())

list_a = []
for i in range(N):
  list_a.append(int(input()))

list_a = sorted(list_a)

list_a.reverse()  

for i in list_a:
  print(i,end=" ")