#Part1. 그리디
#문제 4. 주어진 수 중에서 X라면 X이상으로 그룹 지어서 최대 그룹 수 구하기   
# 5
# 2 3 1 2 2 
# 답 : 2

n = int(input())

list_a = list(map(int,input().split()))

list_a = sorted(list_a)

len_value = len(list_a) 
i = -1
count = 0
while True:
  len_value = len_value - list_a[i]
  i = i - list_a[i]
  count += 1

  if len_value == 0:
    print(count)
    break

#Point
#먼저 정렬한 후 값이 큰것 끼리 묶기
#가장 큰 값으로 시작 후 -> 전체 길이에서 가장 큰 값 빼기 & count+1 -> 그 다음 인덱스 나타내기(i - list_a[i])  -> 반복 (길이 0될때까지) 


#(전체 리스트에서 끝까지 길이 자르는 문제)  -> 백준 그리디) 주유소 문제랑 비슷함!