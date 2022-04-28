#Part2. 구현
#문제 7. 2020 카카오 LV2 문자열 압축

def solution(s):
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step]   #먼저 시작값 설정 (또는 기준값)     
        count = 1
        
        #이전 문자열과 비교하기
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:     #똑같다면
                count += 1
            else:                       #다르다면
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]  #기준값 변경
                count = 1
                
        #남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        #비교
        answer = min(answer, len(compressed))
    return answer
    
#Point 
#자르는 단위가 다른 문제 & 길이 자르는 문제
#1개단위부터 늘려가며 확인 // 최대 반절단위까지만 확인 // 인덱싱으로 푸는 문제
#길이 자르는 문제는 시작값 설정해주고, 나중에 기준값으로 변경함 // 반복문 한번으로 돌기
