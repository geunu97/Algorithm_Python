def solution(s):
    answer = []
    for ss in s:
        stack = []
        count = 0
        for i in ss:
            if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1' and i == '0':
                stack.pop()
                stack.pop()
                count += 1
            else:
                stack.append(i)
        
        
        stack = "".join(stack)
        zero_index = stack.rfind('0')   #(rfind는 배열이 아닌 문자열만 가능) 오른쪽에서부터 가장 가까이 있는 걸 찾아서 인덱스 반환한다.  없다면 -1을 반환한다
        
        if zero_index != -1:
            result = stack[:zero_index+1] + ('110' * count) + stack[zero_index+1:]
        
        else:
            result = ('110' * count) + stack
        
        answer.append(result)
    
    return answer
  

# 스택 응용문제

#1. 스택을 이용해서 배열 앞에서부터 연속된 수 110을 찾아서 빼내고, 110이 몇개 있는지 구한다

#2. 가장 마지막에 있는 0의 바로 오른쪽에 + '110'의 갯수만큼 이어주고 + 나머지 부분 이어서 붙인다 

#3. 0이 하나도 없다면, 가장 처음에 있는 1의 바로 왼쪽에 '110'의 갯수만큼 붙이고, 나머지 부분 이어서 붙인다


#다시 보기!!!