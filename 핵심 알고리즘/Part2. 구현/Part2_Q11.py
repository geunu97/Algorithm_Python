#Part2. 구현
#문제 11. (구현/완전탐색) 치킨 배달 (백준15686)

from itertools import combinations      #헐 풀었다@ㅒㅑ#ㅕ@ㅒ#ㅕㅒ@ㅕ#ㅒ@ㅕ#@ㅑ#ㅒ@ㅑ#ㅓ@#@ㅓ#ㅓ@ㅓ#ㅒ@ㅓ#ㅒ@ㅓ#ㅒㅓ@#ㅒㅓ@#

N,M = map(int,input().split())

list_a=[]
for i in range(N):
  list_b = list(map(int,input().split()))
  list_a.append(list_b)

list_house=[]
list_chicken=[]
for i in range(N):
  for j in range(N):
    if list_a[i][j] == 1:
      list_house.append([i,j])
    elif list_a[i][j] == 2:
      list_chicken.append([i,j])


combinations_ = list(combinations(list_chicken,M))
answer_min=987654321

def distance_(combi_s,list_house):
  sum_value = 0
  global answer_min

  for house in list_house:
    min_value = 987654321
    for combi_ in combi_s:
        distance = abs(house[0]-combi_[0])+abs(house[1]-combi_[1]) 
        min_value = min(min_value,distance)

    sum_value += min_value

  answer_min = min(answer_min,sum_value)


for combi_s in combinations_:
    distance_(combi_s,list_house)


print(answer_min)

#Point
#직접 풀어서 맞은 문제
#조합, BFS() 문제  -> itertools combinations 사용