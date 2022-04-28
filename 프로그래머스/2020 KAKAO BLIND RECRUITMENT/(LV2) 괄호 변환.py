#LV2 괄호변환

#올바른 괄호 문자열인지 확인
def check_(u):
    stack = []
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
    
#재귀함수
def div_(p):
    if len(p) == 0:
        return ''
    
    u = ""
    left_count = 0
    right_count = 0
    for i in p:
        u += i
        if i == '(':
            left_count += 1
        elif i == ')':
            right_count += 1
            
        if left_count == right_count:
            break
    
    v = p[left_count+right_count:]    
    
    
    #분리한 u가 올바른 괄호 문자열인지 확인
    if check_(u) == True:
        return u + div_(v)  #v에 대해 1단계부터 다시 수행한 후 마지막에 u에 더한 후 반환
    
    else:
        str1 = "("
        str1 += div_(v)
        str1 += ')'
        u = u[1:-1]
        reverse_u = ""
        for i in u:
            if i == '(':
                reverse_u += ')'
            else:
                reverse_u += '('
        
        str1 += reverse_u
        return str1
        
def solution(p):
    if check_(p):              #이미 올바른 괄호 문자열이라면
        return p
    else:
        return div_(p)


#Point
#주어진 그대로 구현할 수 있는지 구현 문제 & 재귀함수 문제 & 올바른 괄호 판별(스택) 문제