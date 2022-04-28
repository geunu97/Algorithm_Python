#11단계: 브루트 포스
#3. 덩치 비교하기

a = int(input())

list_a=[]
list_b=[]
list_c=[]

for i in range(a):
    x,y = map(int,input().split())           
    list_a.append(x)                       #입력형태 봐두기
    list_b.append(y)

for j in range(0,a):
    count = 1

    for k in range(0,a):
        if list_a[j] < list_a[k] and list_b[j] < list_b[k]:        # (자기포함) 기준한개당 모두 비교하기
            count += 1

    list_c.append(count)

for s in range(len(list_c)):
    print(list_c[s],end=" ")     # 리스트 없애고 한줄로 출력하기
