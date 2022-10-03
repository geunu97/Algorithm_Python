a = int(input())
name = []
for _ in range(a):
  name.append(input())

name = sorted(name)

answer = ""
count = 1
value = name[0][0] # 첫 값 넣기
for i in range(1,len(name)):
  if value == name[i][0]:
    count += 1
  else:
    if count >= 5:
      answer += value

    value = name[i][0]
    count = 1

#마지막 처리 해줘야함!!
if count >= 5:
  answer += value

if answer == "":
  print("PREDAJA")
else:
  print(answer)