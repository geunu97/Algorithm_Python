#LV2 타겟 넘버

result = 0
def dfs(index,list_a,numbers,target):
    global result
    if len(list_a) == len(numbers):            #재귀) 탈출 조건
        if sum(list_a) == target:
            result += 1
        
        index -= 1
        return
    
    list_a.append(numbers[index])
    dfs(index+1,list_a,numbers,target)    #재귀 2개
    list_a.pop()
    
    list_a.append(-numbers[index])
    dfs(index+1,list_a,numbers,target)    #재귀 2개
    list_a.pop()
        
    
def solution(numbers, target):
    list_a = []
    dfs(0,list_a,numbers,target)
    
    return result



#이게 왜 풀렸네?????????????    wow!
#Point
#dfs문제
#인덱스로 넣어서 앞에서부터 계산해주기, 길이 꽉 차면 종료.계산.돌아가기





