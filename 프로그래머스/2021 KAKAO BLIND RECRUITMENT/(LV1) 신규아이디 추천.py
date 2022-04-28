#LV1 신규아이디 추천

def solution(new_id):
    #1단계
    new_id = new_id.lower()                #특수문자도 포함되어있는상태에서도 상관없음, 특수문자는 변화없음
    
    #2단계
    new_id2 = ""
    for i in new_id:
        if i.isalnum() or i == '-' or i == '_' or i == '.':
            new_id2 += i
    
    #3단계  (2개이상의 .을 1개로 만들기)
    new_id3 = ""
    check = 0
    for i in new_id2:
        if i == '.':
            check = 1
        else:
            if check == 1:
                new_id3 += '.'
                
            new_id3 += i
            check = 0
    #마지막처리
    if check == 1:
        new_id3 += '.'
        
    #4단계
    new_id4 = list(new_id3)
    
    if len(new_id4) >= 1:
        if new_id4[-1] == '.':
            new_id4.pop()
    
    if len(new_id4) >= 1:
        if new_id4[0] == '.':
            new_id4.pop(0)

    #5단계
    if len(new_id4) == 0:
        new_id4.append('a')
    
    #6단계
    if len(new_id4) >= 16:
        new_id4 = new_id4[:15]    #슬라이싱
    
        if new_id4[-1] == '.':
            new_id4.pop()
    
    #7단계
    while True:
        if len(new_id4) >= 3:
            break
        
        new_id4.append(new_id4[-1])
        
    #리스트를 문자열로 변환
    answer = ""
    for i in new_id4:
        answer += i
        
    return answer


#Point
#기본적인 문자열문제