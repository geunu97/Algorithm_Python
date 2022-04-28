#Part5. 이진 탐색
#문제 2. 떡 자르기 , 높이 H를 정해 떡들을 잘라서 적어도 M이상의 떡을 얻어야할 때 최대 높이 H를 구하기 
#       (높이보다 작은 떡은 잘리지 않고 높이보다 큰 떡의 경우 잘린 윗부분을 가져가는 것, ex) 19,14,10,17의 떡들이 있을 때 높이 15로 정하면 4+0+0+2 = 6의 떡을 얻을 수 있다)

n,m = map(int,input().split())
list_a = list(map(int,input().split()))

start = 0   #높이의 최솟값 0으로 설정
end = max(list_a)  #높이의 최댓값으로 설정

result = 0
while start <= end:    #반복문으로 구현
    total = 0
    mid_value = (start + end) // 2   #중간값 설정
    
    for x in list_a:   #높이에 맞게 떡들을 잘라서 합치기
        if x > mid_value:
            total += x - mid_value 

    if total < m:  #갯수에 부족하다면 
        end = mid_value - 1   #왼쪽 범위에서 다시찾기 (더 많이 잘라야 됨,높이를 낮춰야 됨)
    else:  #갯수보다 같거나 많다면
        result = mid_value  #일단 높이(답) 저장, 최댓값을 찾기위해 반복
        start = mid_value + 1  #오른쪽 범위에서 다시찾기  (덜 잘라보기, 높이 올리기)

print(result)

#Point 
#높이를 탐색값으로 설정




