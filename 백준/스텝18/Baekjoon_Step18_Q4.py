#18단계: 스택
#4. 2가지 종류의 괄호있는 문장에서 올바른 괄호인지 판단하기 () []

while True:     #예제 입력 점 하나만 받을 경우에만 종료하라는 뜻이였음
    str = input()

    if str == '.':
        break

    check = 1
    stack= []   #스택하나로 풀기
    for i in str:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i == ']':
            if len(stack) == 0:
                check = 0
                break
            else:
                if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '['):     
                    stack.pop()
                else:  # ( [ ) ]  답은 no
                    check = 0 
                    break

    if len(stack) >= 1:
        check = 0

    if check == 0:
        print('no')
    else:  #완벽한 괄호 (stack에 아무것도 없는 경우)
        print('yes')


