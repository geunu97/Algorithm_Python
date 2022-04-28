#Part1. 그리디
#문제 5.  숫자로 이루어진 하나의 문자열을 입력받으면 + * 로 결과값 최대로 만들기

list_a = list(map(int,input()))

for i in range(len(list_a)-1):
  if list_a[i] != 0 and list_a[i+1] != 0:
    list_a[i+1] = list_a[i] * list_a[i+1] 
  else:
    list_a[i+1] = list_a[i] + list_a[i+1]


print(list_a[-1])

#Point
#0일 때만 더하고 나머지는 곱하면 됨
#다음 인덱스에 결과값 넣기

