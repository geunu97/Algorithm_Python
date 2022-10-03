a = int(input())
pattern = input()
file = []
for i in range(a):
  file.append(input())


#핵심 부분
start_value = pattern[:pattern.index("*")]
end_value = pattern[pattern.index("*")+1:]

for i in file:
  if len(i) >= (len(start_value) + len(end_value)):  #예외처리 i의 길이가 반드시 같거나 더 길어야 한다
    if i[:len(start_value)] == start_value and i[len(i)-len(end_value):] == end_value :
      print("DA")
    else:
      print("NE")
  else:
    print("NE")
  
  

