#7단계: 문자열
#8. 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
#   전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 
#   숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#   숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 
#   위해선 1초씩 더 걸린다.
#   상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 
#   즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#   할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

list_a = list(map(str,input()))

count = 0

for i in range(len(list_a)):
    if list_a[i] == 'A' or list_a[i] == 'B' or list_a[i] == 'C' :
        count += 3
    elif list_a[i] == 'D' or list_a[i] == 'E' or list_a[i] == 'F' :
        count += 4
    elif list_a[i] == 'G' or list_a[i] == 'H' or list_a[i] == 'I' :
        count += 5
    elif list_a[i] == 'J' or list_a[i] == 'K' or list_a[i] == 'L' :
        count += 6
    elif list_a[i] == 'M' or list_a[i] == 'N' or list_a[i] == 'O' :
        count += 7
    elif list_a[i] == 'P' or list_a[i] == 'Q' or list_a[i] == 'R' or list_a[i] == 'S':
        count += 8
    elif list_a[i] == 'T' or list_a[i] == 'U' or list_a[i] == 'V' :
        count += 9
    elif list_a[i] == 'W' or list_a[i] == 'Y' or list_a[i] == 'X' or list_a[i] == 'Z':
        count += 10

print(count)