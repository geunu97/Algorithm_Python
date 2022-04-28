#7단계: 문자열
#5. 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
#   단, 대문자와 소문자를 구분하지 않는다.

a = input()

max_count = 0

for i in range(65,97):
    if a.count(chr(i)) + a.count(chr(i+32)) > max_count :
        max_count = a.count(chr(i)) + a.count(chr(i+32))
        max_chr = chr(i)
    elif a.count(chr(i)) + a.count(chr(i+32)) == max_count and max_count != 0 :
        max_chr = "?"


print(max_chr)




