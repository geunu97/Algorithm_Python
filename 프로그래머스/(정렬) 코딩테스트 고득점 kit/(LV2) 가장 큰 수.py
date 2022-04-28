#LV2 가장 큰 수

def solution(numbers):
    list_a = []
    for number in numbers:
        num = (str(number) * 4)[:4]     
        list_a.append((num, len(str(number))))
    
    list_a = sorted(list_a)[::-1]
    
    if list_a[0][0] == '0000':
        return '0'                #예외처리  [0,0,0]일 때 
    
    else:
        answer = ''
        sum_value = 0
        for num,len_value in list_a:
            answer += num[:len_value]
            
        return answer


#Point
#문제의 핵심은 4자리까지 반복하는 것이다.  (최대 1000이하의 수이기 때문에)     -  가장 중요
#예를 들어) 3 일 경우 3333, 30일 경우 3030, 303일 경우 3033으로 만든다

#그 다음 문자열형식으로 정렬하기

#다시 원래의 길이대로 차례대로 문자열 합치기


#--------------------------------------------------------------------------------------
#노트에 써놓기
#(중요!!!) int형식 정렬과 문자열형식 정렬은 다르다
#(int형식 정렬)   [1, 2, 10, 20]
#(문자열형식 정렬) ['1','10','2','20']  앞에서부터 순서대로 비교한다
