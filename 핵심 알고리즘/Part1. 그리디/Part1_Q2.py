#Part1. 그리디
#문제 2. 각 행마다 가장 작은 수를 찾고 그 중에서 가장 큰 수 찾기
     
n,m = map(int,input().split())

list_a=[]
list_b=[]
for i in range(n):
  list_a.append(list(map(int,input().split())))
  min_value = min(list_a[i])
  list_b.append(min_value)


print(max(list_b))