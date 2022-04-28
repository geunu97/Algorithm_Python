#Part3. DFS,BFS
#문제 5. 카카오 2020 괄호 변환 LV2 (PASS)

#pass
'''
def DFS(w):   
    #분리
    if w == '':
        return w
    else:
        u = ""
        count = 0
        for i in w:
            u += i
            if u.count('(') == u.count(')'):
                break
            count += 1
        
        if count+1 != len(w):
            v = ""
            for i in range(count+1,len(w)):
                v += w[i]
        else:
            v = ""

        #u가 올바른 괄호 문자열인지 확인하기!!!!!!
        stack=[]
        no_value = 0
        for i in u:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0:
                    no_value = 1
                    break
                else:
                    stack.pop()

        if no_value == 0:  # u가 "올바른괄호"
            v = DFS(v)
            

        elif no_value == 1: # u가 "잘못된괄호"
            new_answer = "("
            v = DFS(v)
            new_answer += v
            new_answer += ")"
            u = list(u)
            u.pop(0)
            u.pop()
            u = map(str,u)
            new_u = ""
            for i in u:
                if i == '(':
                    new_u += ')'
                elif i == ')':
                    new_u += '('                    
            new_answer += new_u
            return new_answer


def solution(p):
    print(DFS(p))





solution("()))((()")

#u,v = DFS("()))((()")
'''

#Point
#구현 & 재귀& 
#올바른 괄호인지 확인법 
'''
stack=[]
    no_value = 0
    for i in u:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                no_value = 1
                break
            else:
                stack.pop()
'''
    