#18단계: 스택
#2. 0이면 지우고 0이 아니면 입력 받기


K = int(input())

stack = []
for _ in range(K):
    N = int(input())

    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))