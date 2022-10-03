a,b,c = map(int,input().split())
b = b*2
c = c*3

list_a = []
max_value = -987654321
for i in range(3):
  x,y = map(int,input().split())

  list_a.append([x,y])
  max_value = max(max_value,x,y)

#배열에 넣어서 해당시간 더해주기
time = [0] * (max_value+1)   
for x,y in list_a:
  for i in range(x,y):
    time[i] += 1

answer = 0
for i in time:
  if i == 1:
    answer += a
  elif i == 2:
    answer += b
  elif i == 3:
    answer += c

print(answer)



