#Part2. 구현
#문제 4. (구현/시물레이션) 캐릭터가 방문한 칸의 개수 구하기
#      1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
#      2. 아직 가보지 않은 칸이 존재한다면, 회전한 다음 왼쪽으로 이동한다
#      3. 이미 가본 칸이라면 회전만 하고 2번으로 돌아간다
#      4. 4방향 모두 가본 칸이거나 바다로 되어 있는 경우 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1번으로 돌아간다
#      5. 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
#      -----------------------------------------------------------------------------------------------------------
#       각각의 칸은 육지 or 바다로 되어 있음 (바다로 되어있는 곳은 못감)
#       캐릭터는 동서남북 중 한 곳을 바라보는 곳이 있음 
#       동서남북으로 한칸씩 이동 

n,m = map(int,input().split())

#시작점,바라보는방향
x,y,look = map(int,input().split())

list_list = []
for i in range(n):
  list_a = list(map(int,input().split()))
  list_list.append(list_a)

#초기화
list_new = [[0] * m for i in range(n)]
list_new[x][y] = 1  #현재 좌표 방문 처리 (시작점)

#dx,dy 설정 (왼쪽부터 회전하니깐 순서대로!!!!) (y 아래로가면 +임)
#look과 순서가 맞아야 함
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#방향 -1씩 해주기, -1되면 3(서쪽) 보게 해주기  (0~3)
def turn_left():
  global look
  look -= 1
  if look == -1:   
    look = 3

#무한 반복으로 시작
count = 1
turn_time = 0  #연속 회전 횟수 구하기 위해
while True :
  turn_left()
  nx = x + dx[look]    #여기 표현 중요!!!!
  ny = y + dy[look]    #왼쪽으로 회전  #여기 표현 중요!!!!

  #아직 가보지 않은 칸이고 육지 인지 확인하기
  if list_new[nx][ny] == 0 and list_list[nx][ny] == 0:
    list_new[nx][ny] = 1   #가보지 않았으면 1로 바꾸기
    x = nx    #이제 실제로 이동하기
    y = ny    
    count += 1    #이동횟수
    turn_time = 0    
    continue
  #가본 칸이거나 바다인 경우
  else:
    turn_time += 1  #연속 회전 횟수 

  #4방향 모두 갈 수 없으면 (연속회전 4번 됐으면)
  if turn_time == 4:
    nx = x - dx[look]  #뒤로 한칸 가기 때문에 - 임
    ny = y - dy[look]  

    #뒤로 한칸 있는 곳이 육지인지 확인
    if list_list[nx][ny] == 0:
      x = nx   #육지라면 이동하기
      y = ny
    #바다라면 종료
    else:
      break
    turn_time = 0

print(count)


#Point
#x,y // look // dx,dy // nx,ny 설정해주기     (시작점,현재좌표 // 바라보는 방향 // 이동할 수 있는 칸 // 미리 본 칸)
# dx[look], dy[look] 표현 중요!!
# nx = x + dx[look], ny = y + dy[look] 표현도 중요!!!! 
#dx,dy는 왼쪽부터 90도로 회전하니깐 순서지켜서 써야됨
#2차원 리스트 똑같이 초기화해서 만들고 가본 곳은 1로 설정하기  (2차원리스트 초기화는 리스트내포 표현으로만 사용)
#방향 바라보는 함수 설정해주기 -1씩 , -1되면 3으로
#시물레이션 시작
