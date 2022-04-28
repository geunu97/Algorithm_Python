#LV2 전화번호 목록

def solution(phone_book):
    dictionary = {}
    
    phone_book2 = []
    for i in phone_book:
        phone_book2.append([i,len(i)])
    
    phone_book2 = sorted(phone_book2, key = lambda x: x[1])
    phone_book2.reverse()          
    
    for a,b in phone_book2:
        if a in dictionary:
            return False
        
        for i in range(1,len(a)+1):
            dictionary[a[:i]] = 1
        
    
    return True


#Point
#해쉬 문제 (딕셔너리)

#길이가 긴 순으로 정렬

#앞에서부터 차례대로 길이순으로 쪼개서 차례대로 딕셔너리에 넣기
#딕셔너리에 수가 있으면 그대로 false반환
#마지막 까지 없으면 마지막에 true반환