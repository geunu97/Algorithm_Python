#12단계: 정렬
#6. 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, 
#   x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline 

N = int(input())

list_a=[]
for i in range(N):
    x,y = map(int,input().split())
    list_a.append([x,y])             #하나의 리스트안에 쌍으로 리스트 넣기(이중리스트)   , 딕셔너리 사용 안해도됨

list_a = sorted(list_a, key = lambda x : (x[0],x[1]))#핵심   #0은 앞에, 1은 뒤에
                                                       

for j in range(N):
    print(list_a[j][0],list_a[j][1])

