#LV2 압축

def solution(msg):
    list_a = [0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    answer = []
    i = 0
    while i < len(msg):
        for j in range(len(msg),i,-1):   #가장 긴거부터 찾는게 핵심    #찾은후에 다음 인덱스 가르켜야댐 
            if msg[i:j] in list_a:
                answer.append(list_a.index(msg[i:j]))
                
                list_a.append(msg[i:j+1])
                break   
        
        i = (j-i) + i
    
    #print(list_a)
    #print(answer)
    
    return answer