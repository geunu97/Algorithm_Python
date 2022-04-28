#16단계: 그리디 알고리즘 (탐욕법)
#2. 회의실 배정  

#가능한 많은 회의를 할 수 있게 구해야 되는 문제
n = int(input())

list_a=[]
for i in range(n):
  a,b = map(int,input().split())
  list_a.append([a,b])

list_a = sorted(list_a,key = lambda x: (x[1],x[0]))

value = list_a[0][1]
count = 1

range_value = 1
for i in range(1,len(list_a)):
  if list_a[i][0] >= value:
    value = list_a[i][1]
    count += 1

print(count)

#Point
#시작시간,차이가 아니라 끝나는 시간이 중요!!!    (빨리빨리 끝내야 최대로 많이 할 수 있기 때문에)
#끝내는 시간을 기준으로 정렬한 후, 끝내는 시간이 같으면 시작시간을 정렬하기!!
#끝나는 시간을 구한 후 다음은 시작시간이 끝나는 시간보다 크거나 같은 수 찾기 (반복)
#count 구하기