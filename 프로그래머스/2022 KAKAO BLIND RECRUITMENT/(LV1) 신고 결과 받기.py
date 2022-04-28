#LV1 신고 결과 받기

def solution(id_list, report, k):
    dictionary = {}
    for i in id_list:   #딕셔너리에 초기화
        dictionary[i] = [0,[],0]   #[신고당한 횟수, 이 유저를 신고한 사람이름, 메일 받아야되는 횟수] 형태
        
    
    report = list(set(report))  #중복불가 (똑같은사람이 똑같은사람 신고 1번만 할 수 있음)
    for i in report:  
        i = i.split(' ')  #문자열에서 split()많이 나오네!?!?
        
        dictionary[i[1]][0] += 1 #신고당한 횟수 +1
        dictionary[i[1]][1].append(i[0]) #신고한 사람 이름
        

    #신고당한 횟수가 k번 이상인 이름 찾고, k번 이상 신고당한 사람을 신고한 사람이름의 [2]번째에 +=1 해주기
    for key in dictionary:
        if dictionary[key][0] >= k:
            for i in dictionary[key][1]:
                dictionary[i][2] += 1
    

    #메일 받아야되는 횟수만 순서대로 뽑아내기
    answer = []
    for key in dictionary:
        answer.append(dictionary[key][2])
        
        
    return answer



#Point
#단순 리스트로 풀었더니 시간초과 받았던 문제
#딕셔너리로 풀어야 했던 문제 (해쉬 문제)

