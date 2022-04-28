str = input()

len_value = len(str) // 2

sum1 = 0
sum2 = 0

for i in range(len_value):
    sum1 += int(str[i])

for i in range(len_value,len(str)):
    sum2 += int(str[i])

if sum1 == sum2 :
    print("LUCKY")
else:
    print("READY")

#각 자리수 문제
#리스트로 하나씩 잘라서 받아도 되고, 문자열로 받아서 반복문 돌려도 됨

