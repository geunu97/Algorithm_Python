#삼성 SW 역량 테스트 기출 문제
#1. 시험 감독

import math

N = int(input())
list_a = list(map(int,input().split()))
B,C = map(int,input().split())


sum = N
for i in list_a:
    i = i - B
    if i >= 1:
        sum += math.ceil(i / C)


print(sum)