#9단계: 기본 수학 2
#11번 문제

a = int(input())

for i in range(a):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    if r1 > r2:                   #큰 원 구하기
        a = x1
        b = y1
        c = r1

        x1 = x2
        y1 = y2
        r1 = r2

        x2 = a
        y2 = b
        r2 = c

    d = ((x1 - x2)**2 + (y1-y2)**2)**0.5            #중심 사이의 거리 구하기

    #두 원이 같을 때
    if d == 0 and r1 == r2:    
        print("-1")

    # (두 원이 한 점에서 만날 떄, 외접 or 내접)
    elif d == r1+r2 or r2 == d + r1:
        print("1")

    # (두 원이 만나지 않을 때 - 밖 or 안)
    elif d > r1+r2 or d < r2-r1:
        print("0")

    # 두 점에서 만날 때
    else:
        print("2")