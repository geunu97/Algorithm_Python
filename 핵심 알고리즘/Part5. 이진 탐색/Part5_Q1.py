#Part5. 이진 탐색
#문제 1. 리스트 2개를 입력받아서 하나의 리스트 안에 값 하나씩 다른 리스트에 있는지 확인하기 있으면 yes, 없으면 no


N = int(input())
list_a = list(map(int,input().split()))
M = int(input())
list_b = list(map(int,input().split()))

list_a = sorted(list_a)   #반드시 정렬해주고 시작

answer = []
for i in list_b:
    start = 0    #인덱스값으로 시작값 설정
    end = N-1    #인덱스값으로 끝값 설정
    result = 0

    while start <= end:   #반복문으로 구현하기
        mid_value = (start + end) // 2     #중간값 설정

        if list_a[mid_value] == i:   #탐색 성공
            result = 1
            break

        if list_a[mid_value] < i:
            start = mid_value + 1    #오른쪽 범위에서 다시찾기
        else:
            end = mid_value - 1      #왼쪽 범위에서 다시찾기

    if result == 1:
        answer.append('yes')
    else:
        answer.append('no')

for i in answer:
    print(i,end=" ")



#Point
#이진 탐색, 계수 정렬, set()으로 3가지 풀이법이 가능
