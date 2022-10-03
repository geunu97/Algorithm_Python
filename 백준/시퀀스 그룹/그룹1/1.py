one = '1'

while True:
  try:
    a = int(input())
    one = '1'
    while True:
      if int(one) % a == 0:
        print(len(one))
        break
      
      one += '1'

  except EOFError:    # 예외처리 필수 문제, 끝없이 입력을 받다가, EOFError를 만나면 중지된다
    break


# 백준 문제 -> 입력 갯수 주지 않고, 게속 입력 받기 노트에 써놓기





