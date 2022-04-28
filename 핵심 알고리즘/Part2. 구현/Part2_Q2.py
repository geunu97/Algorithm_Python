#Part2. 구현
#문제 2. 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 구하기
#       (구현/완전탐색)

n = int(input())
  
count = 0
for i in range(n+1):
  for j in range(60):
    for k in range(60):                         #시간 반복문 3개로 표현하기
      if '3' in str(i) + str(j) + str(k):       #str로 모두 붙여서 시간 표현하고, 3 있는지 확인하기
        count += 1

print(count)
  
#Point
#시간 문제(완전 탐색) 반복문 3개로 구현
#특정 숫자나 문자가 들어있는 경우 str(), in으로 확인