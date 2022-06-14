from itertools import permutations

def solution(expression):
	#과정1 연산자 순서, 모든 경우의 수 구하기
    exp = []
    if '*' in expression:
        exp.append('*')
    if '-' in expression:
        exp.append('-')
    if '+' in expression:
        exp.append('+')
    per_exp = list(permutations(exp,len(exp)))
    
    #과정2 연산자와 피연산자 구분해주기
    expression2 = []
    str_value = ""
    for i in expression:
        if i.isdigit() == False:
            expression2.append(str_value)
            expression2.append(i)
            str_value = ""
        else:
            str_value += i
    expression2.append(str_value)
   
   #과정3,4
    answer = -987654321
    for i in per_exp:
        new_expression = []
        for x in expression2:
            new_expression.append(x)
            
        for j in i:
            index = 0
            len_value = len(new_expression)
            while True:
                if index == len_value:
                    break
        
                if new_expression[index] == j:
                    new_expression[index] = str(eval(new_expression[index-1]+j+new_expression[index+1]))
                    new_expression.pop(index+1)
                    new_expression.pop(index-1)
                    len_value -= 2
                    index -= 1          #리스트에서 삭제했기 때문에, 인덱스, 길이 맞춰줘야 한다!
                 
                index += 1
        
        answer = max(answer, abs(int(new_expression[0])))
    

    return answer


'''
1. 처음 주어진 expression의 문자열 안에 * , - , + 가 있는지 확인 후 연산의 순서를 정하기 위해 모든 조합의 경우를 구했습니다
 - [ * , - , +]처럼 있다면 (*,-,+) , (*,+,-) , (+,*,-) ... 처럼 모두 구했습니다

2.  처음 주어진 expression에서 연산자와 피연산자를 구분했습니다
 - "100-200*300-500+20"  이것을  다음과 같이 [100, - , 200 , * , 300 , - , 500 , + , 20]처럼 구분했습니다

3. [핵심] 2번에서 구분한 리스트에서 앞에서부터 해당 연산자가 있는지 확인 후 해당 인덱스-1 과 해당 인덱스+1 번째 수를 해당 연산자로 계산한 수를 해당 인덱스에 삽입했고, 나머지 양쪽의 2개의 인덱스-1, 인덱스+1은 리스트에서 삭제했습니다
 -  100 - 200 이라면 가운데 -자리에 -100을 넣고 양쪽 100과 200을 삭제했습니다

4.  1번에서 조합한 경우의 수를 통해 3번의 과정을 반복하고, 최댓값을 구했습니다
'''