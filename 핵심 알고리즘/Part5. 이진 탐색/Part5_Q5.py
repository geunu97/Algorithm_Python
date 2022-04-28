#Part5. 이진 탐색
#문제 5. 공유기 설치 (백준 2110) // n개의 집 좌표를 받아서 c개의 공유기를 설치하려는데 가장 인접한 두 공유기 사이의 최대 거리 출력하기
# ex) 5 3
#     1 2 8 4 9  일 때  1 4 8 또는 1 4 9에 설치하면 된다   

n, c = map(int, input().split())
list_a = []
for _ in range(n):
    list_a.append(int(input()))

list_a = sorted(list_a) #정렬해주고 시작

start = 1   #간격의 처음값 1로 설정
end = list_a[-1] - list_a[0]   #간격의 마지막 값 (끝값-처음값) 설정
result = 0  #결과 0으로 설정
 
while start <= end:  #반복문으로 구현
    mid_value = (start + end) // 2    #중간값 설정
    first = list_a[0]
    count = 1

    for i in range(1,len(list_a)):
        if list_a[i] >= first + mid_value:    #간격에 맞게 갯수세기
            first = list_a[i]
            count += 1

    if count < c:
        end = mid_value - 1    #왼쪽에서 다시시작

    else:
        result = mid_value 
        start = mid_value + 1  #오른쪽에서 다시시작

print(result)


#간격을 탐색값으로 설정