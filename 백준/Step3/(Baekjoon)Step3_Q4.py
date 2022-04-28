#3단계: for문
#4번 문제

import sys

a = int(input()) 

for i in range(a):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)