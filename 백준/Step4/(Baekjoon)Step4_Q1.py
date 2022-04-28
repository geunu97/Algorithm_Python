#4단계: while문
#1. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

while 1 :
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 :
        break
    print(a+b)