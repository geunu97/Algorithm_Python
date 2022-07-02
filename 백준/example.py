from itertools import permutations

L,R = map(int,input().split())
alpha = list(input().split())
al = ['a','e','i','o','u']

combi = list(permutations(alpha,L))
answer = []
for com in combi:
  mo = 0
  ja = 0
  for i in com:
    if i in al:
      mo += 1
    else:
      ja += 1
  
  if mo >= 1 and ja >= 2:
    check = 1
    for i in range(len(com)-1):
      if com[i] > com[i+1]:
        check = 0
        break
    
    if check == 1:
      answer.append("".join(com))

for i in sorted(answer):
  print(i)

