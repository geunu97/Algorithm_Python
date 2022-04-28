#LV2 예상 대진표
# 1번부터 N번까지 토너먼트에 참가한다. 이 때 A의 번호와 B의 번호가 주어질 때 몇 라운드에서 만나는 지 계산하기

import math

def solution(n,a,b):
    start = 1
    end = n
    len_value = n

    while start <= end:
        mid_value = (start+end) // 2
        count = int(math.log2(len_value))   #2의 지수승 구하기

        if (a <= mid_value and mid_value < b) or (b <= mid_value and mid_value < a):  #반절을 기준으로 서로 양쪽에 있다면
            return count

        if a <= mid_value and b <= mid_value:  #반절을 기준으로 같은 곳에 있다면
            end = mid_value - 1
        
        if a >= mid_value and b >= mid_value:  #반절을 기준으로 같은 곳에 있다면
            start = mid_value + 1

        len_value = len_value // 2


print(solution(8,4,7))


#Point
#이진탐색문제
#반절을 기준으로 서로 다른 방향 양쪽에 있으면 현재 길이의 지수를 구하면 된다 (2의 지수승) 