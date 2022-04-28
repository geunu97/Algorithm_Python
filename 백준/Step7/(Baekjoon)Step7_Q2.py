#7단계: 문자열
#2. N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

#풀이1
a = int(input())
b = input()

sum = 0

for i in b:
    sum += int(i)

print(sum)


'''
#풀이2
a=int(input())
list_a = map(int,input())

print(sum(list_a))
'''


