#Part2. 구현
#문제 1. (1,1) 에서 시작해서 입력받은(L,R,U,D)중에서 받은 대로 1칸씩 이동해서 마지막 인덱스 출력하기   (맨 왼쪽 위에서 시작)
# 동서남북 한칸씩 이동 가능   
# 칸의 크기 밖에 이동 불가
  
n = int(input())

x = 1
y = 1   #시작점 설정해주기

plans = input().split()

dx = [0,0,-1,1]   #동서남북 한칸 설정
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:  #중요!
      nx = x + dx[i]
      ny = y + dy[i]    #이동 좌표 구하기
  
  #공간 밖에 있는 경우(4가지) 무시하기 
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  #공간 안에 있으면 x,y에 값 넣기   
  x = nx
  y = ny

print(x,y)

#Point 
#시작점 설정 x,y
#dx,dy 설정
#nx,ny 설정 (미리 가보기)
#nx = x + dx[i] / ny = y + dy[i] 형태 
#공간 벗어나는 경우(4가지) 조건 설정
#x,y에 nx,ny 값 넣기 (진짜 이동)
