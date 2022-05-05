from itertools import combinations

list_a =[]
for i in range(9):
  list_a.append(int(input()))

list_b = list(combinations(list_a,7))

for i in list_b:
  if sum(i) == 100:
    i = sorted(i)
    for j in i:
      print(j)
    break
    

