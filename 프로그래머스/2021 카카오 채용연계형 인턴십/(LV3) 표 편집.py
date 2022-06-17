def solution(n, k, cmd):
    dictionary = {}
    select = k
    stack = []
    
    for i in range(n):
        if i == 0:
            dictionary[i] = ['Null', i+1]
        elif i == n-1:
            dictionary[i] = [i-1, 'Null']
        else:
            dictionary[i] = [i-1,i+1]   #이전 행, 다음 행
    
    for i in cmd:
        i = i.split(' ')
        
        if i[0] == 'D':
            for _ in range(int(i[1])):
                select = dictionary[select][1] 
            
        elif i[0] == 'U':
             for _ in range(int(i[1])):
                select = dictionary[select][0]            
        
        elif i[0] == 'C':
            if dictionary[select][1] == 'Null':
                dictionary[dictionary[select][0]][1] = 'Null' 
                value = dictionary[select][0]
            
            elif dictionary[select][0] == 'Null':
                dictionary[dictionary[select][1]][0] = 'Null'
                value = dictionary[select][1]
                 
            else:
                dictionary[dictionary[select][0]][1] = dictionary[select][1]
                dictionary[dictionary[select][1]][0] = dictionary[select][0]
                value = dictionary[select][1]
            
            stack.append([select,dictionary[select][0],dictionary[select][1]])   
            del dictionary[select]  
            select = value

        elif i[0] == 'Z': 
            if stack[-1][1] != 'Null':
                dictionary[stack[-1][1]][1] = stack[-1][0]   
            
            if stack[-1][2] != 'Null':
                dictionary[stack[-1][2]][0] = stack[-1][0]                 
            
            dictionary[stack[-1][0]] = [stack[-1][1], stack[-1][2]]            
            stack.pop()
    
    answer = ""
    for i in range(n):
        if i in dictionary:
            answer += 'O'
        else:
            answer += 'X'

    return answer


#딕셔너리, 스택
#딕셔너리 (연결리스트 처럼)

'''
1. 딕셔너리에 { 해당 숫자: [이전 숫자, 다음 숫자] } 를 가리키도록 모두 넣어줍니다
  - 맨 처음 노드의 이전, 맨 마지막 노드의 다음은 가리키는 값이 없습니다

2. (이동) U 또는 D의 경우 select노드부터 가리키는 노드를 반복해서 타고 가면 됩니다 

3. (삭제) C의 경우
  3-1. 해당 노드가 가리키는 이전 노드에서 다음 노드를 가리키는 값을 원래 해당 노드가 가리키는 다음 노드 값으로 변경           합니다   (1  ->  2(X)  ->  3)   (1  ->  3)  
  3-2. 위의 과정을 똑같이 반대로 진행합니다  (1  <-  2(X)  <- 3)   ( 1 <-  3)
      - 이 때, 처음 노드가 가리키는 이전값, 마지막 노드가 가리키는 다음값은 없기 때문에 유의합니다
  3-3. 해당 노드를 삭제해줍니다
  3-4. 스택에 삭제했던 노드의 정보를 넣어줍니다
  3-5. select 선택된 노드는 다음 노드를 가리키게 해주고, 마지막 노드의 경우 문제에서 요구한 대로 이 때는 이전 노드를           가리켜야 합니다

  4. (복구) Z의 경우
   4-1. (가장 최근에 삭제했던) 스택의 마지막 원소를 이용해서 삽입해줍니다
      - 이 때도, 처음 노드, 마지막 노드일 때를 유의합니다
   4-2. 3번 과정과 비슷하게 해당 노드와 연결되어 있었던 노드들이 가리키는 값을 원래대로 변경해줍니다

  5. 마지막에 딕셔너리에 있는 노드들이 존재한 것이기 때문에 차례대로 답을 도출해내면 됩니다
'''