#19단계: 큐, 덱
#7. RDD 뒤집거나 첫 번째 원소 제거하기

from collections import deque

t = int(input())

for i in range(t):
    p = input().rstrip()
    n = int(input())
    list_a = input()[1:-1].split(',')  
    que = deque(list_a)

    reverse, flag = 0, 0

    if n == 0: #n==0일 경우 "[]"만 존재할 때
        que = []

    for j in p:
        if j == 'R':
            reverse += 1
        else:
            if len(que) < 1: #error 출력해야할 경우 즉, que에 아무것도 없는데 D일 경우
                flag = 1
                print('error')
                break

            else:
                if reverse % 2 == 0: #reverse가 짝수일 경우
                    que.popleft() #앞에서 제거
                else: #홀수일 경우
                    que.pop() #뒤에서 제거

    if flag == 0:
        if reverse % 2 == 0:
            print('[' + ','.join(que) + ']')
        else:
            que.reverse() #홀수일 경우 뒤집어주기
            print('[' + ','.join(que) + ']')
    
    

#Point
#매번 reverse를 해주지 말기 (시간초과)

#



#list_a = input()[1:-1].split(',')

#print(list_a)

