#9단계: 기본 수학 2
#7번 문제

x,y,w,h = map(int,input().split())

print(min(x,y,w-x,h-y))

'''
#대각선 길이까지 생각함, 잘못된 생각
if x >= w - x:
    xx = w - x
else:
    xx = x

if y >= h - y:
    yy = h - y
else:
    yy = y 

min = min(xx,yy,(xx*xx+yy*yy)**0.5)     #min() 내장함수 사용  #제곱근 사용

print(min)

'''