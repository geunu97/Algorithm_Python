#15단계: 이분 탐색(이진 탐색)
#4. 나무 자르기, 높이를 정하여 나무를 잘라서 잘라진 윗부분을 가져가서 M이상 만들기 이떄 높이의 최댓값 구하기


N,M = map(int,input().split())
list_a = list(map(int,input().split()))

list_a = sorted(list_a)

start = 0          #시작값을 높이의 최소값 0 설정 
end = list_a[-1]   #끝값을 높이의 최댓값 설정

result = 0
while start <= end:
    mid_value = (start + end) // 2

    sum = 0
    for i in list_a:
        if i > mid_value:
            sum += i - mid_value
        else:
            continue

    if sum >= M:
        result = mid_value
        start = mid_value + 1
    else:
        end = mid_value - 1

print(result)


#Point
#높이를 탐색값으로 설정

#이전 떡 자르기 문제와 매우 비슷