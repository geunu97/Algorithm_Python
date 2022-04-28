#18단계: 스택
#5. 스택 수열

n = int(input())

stack = []
answer = []
count = 1
result = True
for _ in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        result = False

if result == False:   #불가능한 경우
    print('NO')
else:
    for i in answer:
        print(i)


