n = int(input())

answer = 0
for i in range(n):
  s = input()

  stack = [s[0]]
  for j in range(1,len(s)):
    if len(stack) > 0:
      if stack[-1] == s[j]:
        stack.pop()
        continue

    stack.append(s[j])
  
  if len(stack) == 0:
    answer += 1

print(answer)
    


#WoW 문제 이해하기 어렵넹
#문제
# A는 다른A 1개와 이어 준다 (A 바로 위에 U모양을 뒤집어서 이어준다는 말)  
# B는 다른B 1개와 이어 준다 (B 바로 위에 U모양을 뒤집어서 이어준다는 말) 

# 그러면 A-A쌍이 여러개, B-B쌍이 여러개 존재할 수 있다

# 여기서 U모양을 그렸을 때 U모양과 다른 U모양이 겹치는게 없으면 좋은 단어라는 말이다


#스택 문제