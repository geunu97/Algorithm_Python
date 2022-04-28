#15단계: 이분 탐색(이진 탐색)
#1. 수 찾기


N = int(input())
list_a = list(map(int,input().split()))

M = int(input())
list_b = list(map(int,input().split()))

list_a = sorted(list_a)   #반드시 정렬된 상태로 시작

for i in list_b:
    result = 0
    start = 0   #인덱스 값으로 시작값 설정
    end = N-1   #인덱스 값으로 끝값 설정

    while start <= end:
        mid_value = (start + end) // 2     #중간값 설정

        if list_a[mid_value] == i:
            result = 1
            print('1')
            break

        if list_a[mid_value] < i:
            start = mid_value + 1
        else:
            end = mid_value - 1
    if result == 0:
        print('0')
        

#정답~.~