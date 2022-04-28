#18단계: 스택
#1. 오큰수

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 수열 입력받기
result = [-1 for _ in range(N)] # 결과값 저장 (오큰수가 없으면 -1이므로 미리 -1로 설정해놓는다)
stack = [] # index를 저장할 스택

stack.append(0) # 첫번째 index 0을 저장한다

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]: # 스택이 비어있지 않고 오큰수가 있다면
        result[stack[-1]] = A[i] # 결과값을 오큰수로 바꿔주고
        stack.pop() # 스택에서 오큰수가 있는 수의 index를 pop
    stack.append(i) # 그 다음 index를 push

for i in result: # 출력
    print(i, end = " ")


#?

