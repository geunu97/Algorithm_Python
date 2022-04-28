#LV2 오픈채팅방

def solution(record):
    result = []
    dictionary = {}
    for i in record:
        i = i.split(' ')
        
        if i[0] == 'Enter':
            dictionary[i[1]] = i[2]
            result.append([i[1],'님이 들어왔습니다.'])
        
        elif i[0] == 'Leave':
            result.append([i[1],'님이 나갔습니다.'])
        
        elif i[0] == 'Change':
            dictionary[i[1]] = i[2]
    
    answer = []
    for i in result:
        answer.append(dictionary[i[0]]+i[1])     #딕셔너리 반복문 돌려서 맞는 키값 찾지 말고, 한번에 바로 키값에 맞는 value값 찾아야 함  (시간 초과 났었음)
    
    
    return answer


#Point
#딕셔너리 이용(해쉬 문제)