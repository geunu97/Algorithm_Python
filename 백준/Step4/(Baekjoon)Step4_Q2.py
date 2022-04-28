#4단계: while문
#2. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

while True :
    try:
        a,b = map(int,sys.stdin.readline().split())
        print(a+b)
    except:
        break


