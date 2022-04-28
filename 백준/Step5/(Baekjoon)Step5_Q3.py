#5단계: 1차원 배열
#3. 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 
#   구하는 프로그램을 작성하시오.
#   예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 
#   계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

#풀이1
'''
a = int(input())
b = int(input())
c = int(input())

n = a * b * c

list_a=[]
number = [0,0,0,0,0,0,0,0,0,0]

list_a.append(n % 10)
list_a.append(n % 100 // 10)
list_a.append(n % 1000 // 100)
list_a.append(n % 10000 // 1000)
list_a.append(n % 100000 // 10000)
list_a.append(n % 1000000 // 100000)
list_a.append(n % 10000000 // 1000000)

if n >= 100000000 :
    list_a.insert(7,n % 100000000 // 10000000)
    list_a.insert(8,n % 1000000000 // 100000000)
elif n >= 10000000 :
    list_a.insert(7,n % 100000000 // 10000000)

list_len = len(list_a)

for i in range(list_len):
    for j in range(10):
       if list_a[i] == j:
            number[j] = number[j] + 1

for k in range(10):
    print(number[k])
'''

#풀이2
a = int(input())
b = int(input())
c = int(input())

n = list(map(int,(str(a*b*c))))

for i in range(10):
    print(n.count(i))
