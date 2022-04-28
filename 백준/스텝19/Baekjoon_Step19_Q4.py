#19단계: 큐, 덱
#4. 프린터큐

from collections import deque

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    list_a = list(map(int,input().split()))

    for i in range(N):    #큐에 값 하나더 넣어주기
        if i == M:
            list_a[i] = [list_a[i], 1]       #원하는 값에만 1로 해주기
        else:
            list_a[i] = [list_a[i], 0]

    answer = []
    q = deque(list_a)
    while True:
        if len(q) == 1:   
            answer.append(q.popleft())
            break

        check = 0
        for i in range(1,len(q)):
            if q[0][0] < q[i][0]:
                q.append(q.popleft())
                check = 1
                break

        if check == 0:
            answer.append(q.popleft())

    count = 1
    for x,y in answer:
        if y == 1:  #원한는 원소의 순서 출력하기
            print(count)
        count += 1


#맨 앞 원소 기준으로 오른쪽에 더 큰 값이 있을 때 popleft -> append (빼서 뒤에 붙이기)
#맨 앞 원소 기준으로 오른쪽에 더 큰 값이 없다면 answer에 먼저 넣어주기 (순서)