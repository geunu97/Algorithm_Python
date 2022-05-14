s = input()

answer =""
for i in s:
  if i.isalpha():
    if 97 <= ord(i) <= 109:   #소문자 중에서 반절
      answer += chr(ord(i)+13)
    elif 110 <= ord(i) <= 122: #소문자 중에서 나머지 반절
      answer += chr(ord(i)-13)

    elif 65 <= ord(i) <= 77:   #대문자 중에서 반절
      answer += chr(ord(i)+13)
    elif 78 <= ord(i) <= 90: #대문자 중에서 나머지 반절
      answer += chr(ord(i)-13) 
  else:
    answer += i

print(answer)