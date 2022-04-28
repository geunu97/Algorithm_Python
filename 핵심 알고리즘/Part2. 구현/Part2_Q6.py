str = input()

list_a=[]
sum=0
for i in str:
    if i.isalpha():             
        list_a.append(i)
    else:
        sum += int(i)

list_a = sorted(list_a)

list_a.append(sum)

for i in range(len(list_a)):
    print(list_a[i],end="")


#같은 문자열 자료형에서 문자인지 숫자인지 구별법!!!!!!!!!!!!!!!!
# i.isalpha()

