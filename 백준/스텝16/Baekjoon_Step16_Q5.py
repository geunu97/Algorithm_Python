#16단계: 그리디 알고리즘 (탐욕법)
#5. 주유소

n = int(input())

list_distance = list(map(int,input().split()))
list_city = list(map(int,input().split()))

value = list_city[0]             #시작값 값 넣기
result = 0

for i in range(0,len(list_city)-1):
  if value > list_city[i]:
    value = list_city[i]          #다음 값이 더 작을때까지 찾아서 그 때 value에 넣기

  result += list_distance[i] * value    #게속 value에 거리 값 곱하기

print(result)


#Point
#위에 메모해둔거 전부
#다음 값이 작은거 나올때까지 전에 가장 작은 값에서 모두 넣어야 됨
#시작값 설정해야댐
#전체 한번만 돌면 끝나고, 조건에 따라 기준점이 다음으로 바뀌어야 되니깐 (반복문 1번 사용 + 기준값 사용)!!!!! 



