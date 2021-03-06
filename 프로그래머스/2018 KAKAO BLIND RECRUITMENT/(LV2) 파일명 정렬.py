#LV2 파일명 정렬
'''
def solution(files):
    list_a = []
    
    for i in files:
        head = ""                  
        number = ""           #리스트로 받는것보다 ""문자열로 받는게 편함,   문자열은 += // 리스트는 append
        tail = ""
        
        for j in i:
            if j.isdigit() == False and len(number) == 0:
                head += j
            elif j.isdigit() and len(number) <= 5:
                number += j
            
            elif j.isdigit() == False and len(number) >= 1:
                break
    
        tail += i[(len(head)+len(number)):len(i)]         #꼬리는 나머지 부분
                
        list_a.append([i,head,number,tail,head.upper(),int(number)])    #정렬하기 위해
    
    list_a = sorted(list_a, key = lambda x: (x[4],x[5]))
    #print(list_a)
    
    answer =[]
    for i in list_a:
        answer.append(i[0])

    return answer
'''

#2번째 풀이
def solution(files):
    index = 0
    result = []
    for i in files:
        head = ""
        number = ""
        tail = ""
        
        for j in i:
            if len(number) > 0 and j.isdigit() == False:
                break
            
            elif j.isdigit() == False:
                head += j
                
            elif j.isdigit() and len(number) <= 5:
                number += j
            
        tail = i[len(head)+len(number):]
        result.append([head.upper(),int(number),tail,i,index])
        index += 1
    
    result = sorted(result, key=lambda x: (x[0],x[1],x[4]))
    answer = []
    for i in result:
        answer.append(i[3])
        
    return answer