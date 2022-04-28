#9단계: 기본 수학 2
#9. 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 
#   주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while True:
    a,b,c = map(int,input().split())         
                       
    min_ = min(a,b,c)
    max_ = max(a,b,c)

    if a == min_:
        if b == max_:
            mid = c
        else:
            mid = b
    elif b == min_:
        if a == max_:
            mid = c
        else:
            mid = a
    elif c == min_:
        if a == max_:
            mid = b
        else:
            mid = a

    if a == 0 and b == 0 and c == 0:
        break

    elif min_*min_ + mid*mid == max_*max_:
        print("right")

    else:
        print("wrong")


# 굳이 1,2,3 번쨰 값 구하지 않고 최대값만 구해도 됨
# 값이 순서대로 주어지는 문제가 아니였음
