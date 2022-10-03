from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    count = 0
    answer = 0
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    while True:
        if count == len(q2) * 3:
            return -1

        if sum_q1 > sum_q2:
            value = q1.popleft()
            q2.append(value)
            sum_q1 -= value
            sum_q2 += value
            answer += 1
        elif sum_q1 < sum_q2:
            value = q2.popleft()
            q1.append(value)
            sum_q2 -= value
            sum_q1 += value        
            answer += 1
        elif sum_q1 == sum_q2:
            return answer
        
        count += 1

'''
두 개의 큐가 있을 때, 두 개의 큐의 합이 같을 때까지 큐의 왼쪽 원소를 빼서 다른 큐의 오른쪽에 넣는 문제
'''

#1. (핵심) 두개의 큐의 합을 비교하여, 합이 큰 큐에서 원소를 빼서 -> 작은 큐에 원소를 넣는다.
#2. 처음 큐의 길이의 3배만큼만 계산하면 된다.
#3. (핵심) 매번 sum()합을 구하지 않고, 슬라이딩 윈도우 사용하여 합을 계산해준다.



