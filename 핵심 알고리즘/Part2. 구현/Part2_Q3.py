#Part2. 구현
#문제 3. L자 형태로 이동하는 말이 있을 때 시작 위치가 주어지면 이동할 수 있는 경우의 수 구하기

list_a = list(input())

#a,b,c,d,e,f,g,h로 되어 있을 때 숫자로 바꾸기
list_al = ['a','b','c','d','e','f','g','h']

for i in range(8):
  if list_a[0] == list_al[i]:
    x = i + 1
    break

#시작 좌표 구하기 (1,1로 시작)
y = int(list_a[1])

#이동가능한 좌표 구하기
dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

count = 0
for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]

  #공간을 벗어나는 4가지 경우의 수 
  if nx < 1 or ny < 1 or nx > 8 or ny > 8: 
    continue
  else:
    count += 1

print(count)


#Point
#행열이 영문으로 주어지는 문제 -> 처음에 숫자로 바꿔주기
# x,y // dx,dy // nx,ny // 공간을 벗어나는 조건4가지   모두 정의해주기!!