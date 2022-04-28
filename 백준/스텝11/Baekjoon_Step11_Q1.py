#11단계: 브루트 포스      (완전탐색 알고리즘)
#1. 블랙잭   

#리스트에서 3개 돌리기!!

N,M = map(int,input().split())

list_a = list(map(int,input().split()))

finish = 0
max = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if list_a[i] + list_a[j] + list_a[k] > M:
                continue
            elif list_a[i] + list_a[j] + list_a[k] == M:  
                print(M)
                finish = 1
                exit()        #반복문 전체 종료
            else :
                if max < list_a[i] + list_a[j] + list_a[k]:
                    max = list_a[i] + list_a[j] + list_a[k]

if finish != 1:
    print(max)