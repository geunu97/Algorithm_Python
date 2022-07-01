s = input()

#딕셔너리로 문자:개수 받기
dictionary = {}
for i in s:
  if i in dictionary:
    dictionary[i] += 1
  else:
    dictionary[i] = 1

#조건1: 전체 길이가 짝수일 때, 각 문자도 짝수개 여야 한다
if len(s) % 2 == 0:
  result = True
  for key in dictionary:
    if dictionary[key] % 2 != 0:
      result = False

#조건2: 전체 길이가 홀수일 때, 각 문자 중 1개만 홀수개, 나머지는 짝수개 여야 한다
else:
  count = 0
  for key in dictionary:
    if dictionary[key] % 2 != 0:
      count += 1
  
  if count == 1:
    result = True
  else:
    result = False

#조건이 성립할 때 팰린드롬 만들기
if result:
  tup = sorted(dictionary.items())    #사전 순으로 출력하기 위해, 딕셔너리 키 기준으로 정렬하기, 리스트 튜플 형태로 반환된다

  list_a = []
  for tu in tup:   #튜플은 값을 변경할 수 없어서, 리스트로 변환하기
    list_a.append(list(tu))

  mid_value=""
  for k in range(len(list_a)):   #홀수개로 가운데 값 구하고, 모두 개수 2로 나눠주기
    if list_a[k][1] % 2 != 0:
      mid_value =list_a[k][0]

    list_a[k][1] = list_a[k][1]//2

  answer = ""
  for st,num in list_a:
    if len(s) // 2 == len(answer):     #반절까지만 구하기
      break
    else:
      answer += (st * num)    # 앞에서부터 문자 * 개수 해주기

  print(answer + mid_value + answer[::-1])   #반절 + 중간 값 + 거꾸로 반절 


#조건이 성립안할 때
else:
  print("I'm Sorry Hansoo")




