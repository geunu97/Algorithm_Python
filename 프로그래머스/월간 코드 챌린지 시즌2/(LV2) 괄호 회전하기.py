#LV2 괄호 회전하기

from collections import deque

#올바른 괄호 문자열인지 확인
def check_(rotate_s):
    stack = []     #스택 리스트 1개만 있어도 됨
    for i in rotate_s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
            
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
        elif i == ']':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '[':
                    stack.pop()
        elif i == '}':
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == '{':
                    stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
    
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.append(s.popleft())
        if check_(s):
            answer += 1

    return answer


#Point
#스택 & 큐 문제