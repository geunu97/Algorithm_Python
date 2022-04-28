#12단계: 정렬
#9. 나이순 정렬

import sys
input = sys.stdin.readline

N = int(input())

list_a=[]
count = 1
for i in range(N):
    x,y = input().split()
    x = int(x)
    list_a.append([x,y,count])    #3개 넣기 핵심
    count += 1

list_a = sorted(list_a, key = lambda x : (x[0],x[2])) 

for j in range(N):
    print(list_a[j][0],list_a[j][1])
