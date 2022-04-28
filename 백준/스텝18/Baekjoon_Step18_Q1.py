#18단계: 스택
#1. 명령어 5가지

import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    list_a = list(input().split())
    
    if len(list_a) == 2:
        stack.append(int(list_a[1]))
    else:
        if list_a[0] == 'top':
            if len(stack) == 0:
                print('-1')
            else:
                print(stack[-1])

        elif list_a[0] == 'size':
            print(len(stack))

        elif list_a[0] == 'empty':
            if len(stack) == 0:
                print('1')
            else:
                print('0')

        elif list_a[0] == 'pop':
            if len(stack) == 0:
                print('-1')
            else:
                print(stack.pop())
        
