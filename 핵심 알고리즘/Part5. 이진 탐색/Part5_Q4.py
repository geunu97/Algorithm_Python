#Part5. 이진 탐색
#문제 4. 주어진 리스트에서 고정점 찾기(인덱스와 값이 동일한 원소) // 1개만 존재


N = int(input())
list_a = list(map(int,input().split()))

start = 0   #인덱스를 시작점으로
end = N-1   #인덱스를 끝점으로

result = 0
while start <= end:
    mid_value = (start + end) // 2    #중간값 설정

    if list_a[mid_value] == mid_value:   #탐색 성공
        print(list_a[mid_value])
        result = 1
        break

    if list_a[mid_value] < mid_value:  
        start = mid_value + 1    #오른쪽 범위에서 다시찾기
    else:          
        end = mid_value - 1      #왼쪽 범위에서 다시 찾기

if result == 0:
    print('-1')

#Point
#고정점을 탐색값으로
