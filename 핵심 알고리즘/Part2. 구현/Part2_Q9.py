#Part2. 구현
#문제 9. (구현/시물레이션) 뱀 이동게임 

from collections import deque

N = int(input())
K = int(input())

#사과 있는 곳 표시
list_a =[[0] * N for _ in range(N)]
for i in range(K):
  a,b = map(int,input().split())
  list_a[a-1][b-1] = 1            

#방향 저장 리스트
L = int(input())
list_L=[]
for i in range(L):
  a,b = input().split()
  list_L.append([int(a),b]) 

#바라보는 방향 (동서남북)
look = 0 #동쪽부터 시작
#dx,dy 설정 (look에 맞게 설정)
dx = [0,-1,0,1]
dy = [1,0,-1,0]
time_ = 0
j = 0
 
baam = [[0,0]]      #현재 뱀이 있는 위치   #문제는 1,1로 시작이지만 (0,0)으로 시작하기
baam = deque(baam)  #덱으로 변환  

#시물레이션 시작
while True:
  nx = baam[0][0] + dx[look]  #처음은 동쪽으로 이동 시작
  ny = baam[0][1] + dy[look]  #정해지면 한방향으로 가기 때문에

  #공간을 벗어나는 경우 Stop
  if nx < 0 or nx >= N or ny < 0 or ny >= N:
    break 

  #자기 자신의 몸과 부딪히는 경우 stop
  if [nx,ny] in baam:      #이중리스트에 리스트가 있다면
    break

  #앞에 사과가 있으면
  if list_a[nx][ny] == 1:
    list_a[nx][ny] = 0    #일단 사과 없애기

  #앞에 사과가 없으면
  else:
    baam.pop()   #baam의 가장 오른쪽 빼기 (큐)

  baam.appendleft([nx,ny]) #baam의 가장 왼쪽에 넣기 (큐)
  #baam에는 앞으로 이동하는 칸은 가장 왼쪽에 있고 가장 뒤쪽 꼬리부분은 가장 오른쪽에 위치해있음 
  #큐 -> 사과 없으면 이동하고 꼬리 짜르고 이동하고 꼬리짜르고 # [[0,1],[0,0]] -> [[0,1], X ] -> [[0,2],[0,1]]

  time_ += 1

  #방향 전환
  if j < L and time_ == list_L[j][0]:
    if list_L[j][1] == 'L':
      look = (look+1) % 4
    elif list_L[j][1] == 'D':
      look = (look+3) % 4
    j += 1

print(time_+1)

#Point
#뱀의 길이가 변할수도 있으면서 이동하기 때문에 -> 큐 사용!!!