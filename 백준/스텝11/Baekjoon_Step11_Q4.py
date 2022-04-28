#11단계: 브루트 포스
#4. 체스판

N,M = map(int,input().split())

list_a = []

for i in range(N):
    list_a.append(input())

result_list = []

for n in range(N-7):                   #반복문 4개 사용해서 => 8*8씩 사각형 돌아가면서 선택하기
    for m in range(M-7):
        first_W = 0
        first_B = 0
        
        for i in range(n,n+8):
            for j in range(m,m+8):
                if (i + j) % 2 == 0:      # 8*8 사각형 안에서 한칸씩 띄어서 선택하는 법!!!! 
                    if list_a[i][j] != 'W':
                        first_W = first_W + 1              #처음이 W일 때   ---- 가정 1
                    if list_a[i][j] != 'B':
                        first_B = first_B + 1              #처음이 B일 떄   ---- 가정 2
                else:
                    if list_a[i][j] != 'B':             
                        first_W = first_W + 1              #처음이 W일 때   ---- 가정 1
                    if list_a[i][j] != 'W':
                        first_B = first_B + 1              #처음이 B일 때   ---- 가정 2
        result_list.append(first_W)
        result_list.append(first_B)
print(min(result_list))               #최솟값 선택