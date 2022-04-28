#LV2 짝지어 제거하기

def solution(s):
    s = list(s)
    stack = [0]


    for i in s:
        if stack[-1] == i:   #스택의 마지막 원소랑 바로 다음 문자 비교하기   #핵심!!
            stack.pop()   #같다면 스택의 마지막원소 제거
        else: 
            stack.append(i)  #다르다면 스택에 넣기
    
    if stack[-1] == 0:   #모두 제거
        return 1
    else:
        return 0 

print(solution('baabaa'))



#Point
#stack 문제
#같은거2개 찾을 때마다 제거해주고 다시 첫 번째 원소로 돌아가서 탐색하면 시간초과!!!




