#3단계: for문
#8. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

a = int(input())

for i in range(a):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #%d: %d + %d ="%(i+1,a,b),a+b)       #format함수로도 가능