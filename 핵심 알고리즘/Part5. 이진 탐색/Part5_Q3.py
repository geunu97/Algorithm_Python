#Part5. 이진 탐색
#문제 3. 오름차순으로 정렬된 리스트에서 주어진 x가 몇개있는지 확인하기 (순차탐색으로 하면 시간초과)

from bisect import bisect_left, bisect_right

N,x = map(int,input().split())
list_a = list(map(int,input().split()))

def count_by_range(left_value,right_value):
    left_ = bisect_left(list_a,left_value)
    right_ = bisect_right(list_a,right_value)

    return right_ - left_


if count_by_range(x,x) == 0:
    print('-1')
else:
    print(count_by_range(x,x))


#Point
#from bisect import bisect_left, bisect_right 사용
