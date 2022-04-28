#12단계: 정렬
#7. 좌표 정렬하기2

import sys
input = sys.stdin.readline

N = int(input())

list_a=[]
for i in range(N):
    x,y = map(int,input().split())
    list_a.append([x,y])

list_a = sorted(list_a,key = lambda x: (x[1],x[0])) #핵심

for i in range(N):
    print(list_a[i][0],list_a[i][1])

