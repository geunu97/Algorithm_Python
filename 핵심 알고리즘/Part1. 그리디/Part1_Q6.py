#Part1. 그리디
#문제 6. (백준 1439번) 문자열 뒤집기
#가장 조금 뒤집어서 모두 숫자 같게 만드는 최소횟수는?   (조건: 연속된 숫자는 1번으로 한다)
#0001100  -> 답: 1번

list_a = list(map(int,input()))

count_0 = 0
count_1 = 0

#시작값 따지기 (시작 숫자에 따라 +1 되고 시작!!)
if list_a[0] == 0:                  
  count_0 = 1
else:
  count_1 = 1

for i in range(len(list_a)-1):
  if list_a[i] == list_a[i+1]:         
    continue
  else:
    if list_a[i+1] == 0:
      count_0 += 1
    else:
      count_1 += 1

print(min(count_0,count_1))

#Point
#시작값 건드는 문제!! (시작값에 따라 +1 됨)
#(0에서 1로 바뀔때, 1에서 0으로 바뀔 때) 2개 설정해줘야 됨!!!!  


