#7단계: 문자열
#3. 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
#   각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
#   포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

list_a = list(map(str,input()))

for i in range(97,123):
    for j in range(len(list_a)):
        if chr(i) == list_a[j]:
            print(j,end=" ")
            break

    if chr(i) not in list_a:
        print("-1",end=" ")


    

