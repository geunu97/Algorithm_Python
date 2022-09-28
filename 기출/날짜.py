#설명
# 1/1 ~ 12/31
# 7일 간격
# 2월은 28일까지 (윤년아님)
# 주어진 달 1 <= month <= 12, 주어진 날짜 0 < date
# 매월 1일 '월/1' 형태
# 정답의 첫번째 인덱스 '월/일' 형태

#문제
# X월 X일이 있는 주 구하기
# 3월 2일 -> ['2/26','27','28','3/1','2','3','4']

#예외
# 2월 29일, 1월 32일 (없는 날짜 줄 수도 있음)
# 12월 31일까지 출력



def solution(month,date):
  # 1. 매월 마지막 날짜 선언
  month_date = [31,28,31,30,31,30,31,31,30,31,30,31]


  # (예외) 없는 날짜 일 경우
  if month_date[month-1] < date:
    return "없는 날짜입니다."

  # (예외) 12월 31일 일 경우
  if month == 12 and date == 31:
    return ["12/31"]


  #2. (핵심) 1월 1일을 기준으로 주어진 날짜까지 몇 일이 지났는지 계산하기
  diff_date = 0
  #달
  for i in range(0,month-1):
    diff_date += month_date[i]
  #일
  diff_date += date-1


  #3. (핵심) 7일 중 몇 번째에 해당하는 지 구하기 (여기서 요일을 구할 수도 있다.)
  result_index = diff_date % 7


  #4. 해당 주 초기화 및 주어진 날짜 넣기
  answer = [0] * 7
  answer[result_index] = date 


  #5. 해당 주 이전 날짜 채우기
  before_date = date-1
  for i in range(result_index-1,-1,-1):
    if before_date == 0:
      before_date = month_date[month-2]

    answer[i] = before_date
    before_date -= 1


  #6. 해당 주 다음 날짜 채우기
  after_date = date+1
  for i in range(result_index+1,7):
    if after_date == month_date[month-1]+1:
      after_date = 1

    answer[i] = after_date 
    after_date += 1


  #7. (조건에 맞게 출력)
  for i in range(len(answer)):
    # (조건1) 매월 1일 '월/1' 형태
    if answer[i] == 1:
      if 1 <= date <= 7:
        answer[i] = str(month) + '/' + str(answer[i])
      else:
        answer[i] = str(month+1) + '/' + str(answer[i])
    
    # (조건2) 정답의 첫번째 인덱스 '월/일' 형태
    elif i == 0:
      if answer[i] > date:
        answer[i] = str(month-1) + '/' + str(answer[i])
      else:
        answer[i] = str(month)  + '/' + str(answer[i])
    
    # 문자열로 변환
    else:
      answer[i] = str(answer[i])
  
  return answer




for i in range(1,13):
  for j in range(1,32):
    print(solution(i,j))


'''
  1: [['1/1',2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,'2/1',2,3,4]],
  2: [[29,30,31,'2/1',2,3,4],[5,6,7,8,9,10,11],[12,13,14,15,16,17,18],[19,20,21,22,23,24,25],[26,27,28,'3/1',2,3,4]],
  3: [[26,27,28,'3/1',2,3,4],[5,6,7,8,9,10,11],[12,13,14,15,16,17,18],[19,20,21,22,23,24,25],[26,27,28,29,30,31,'4/1']],
  4: [[26,27,28,29,30,31,'4/1'],[2,3,4,5,6,7,8],[9,10,11,12,13,14,15],[16,17,18,19,20,21,22],[23,24,25,26,27,28,29],[30,'5/1',2,3,4,5,6]]
'''