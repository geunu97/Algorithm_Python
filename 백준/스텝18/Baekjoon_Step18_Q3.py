#18단계: 스택
#3. 올바른 괄호인지 판단하기

T = int(input())

for _ in range(T):
    str = input()

    check = 1
    stack = []
    for i in str:
        if i == '(':   # ( 일때 넣기
            stack.append(i)
        elif i == ')':   # )일 때 1개 이상 있을 때 빼기
            if len(stack) == 0:  # 아무것도 없으면 올바른 괄호 아님   (조건1)
                check = 0
                break
            else:
                stack.pop()

    if len(stack) >= 1:  # (()  모든 계산 후에 하나 남는 경우 (조건2)
        check = 0

    if check == 0:
        print('NO')
    elif check == 1 and len(stack) == 0:   #모든 계산 후에 하나도 없는 경우 (올바른 괄호)
        print('YES')
