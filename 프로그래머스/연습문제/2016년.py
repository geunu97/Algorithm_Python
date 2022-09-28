
#방법1. 실제 날짜 문제일 때 or 라이브러리 사용하지 않는 조건 없으면 라이브러리 사용해도 될 듯
#datetime 사용법- https://reakwon.tistory.com/172
import datetime

def solution(a, b):
    return datetime.datetime(2016,a,b).strftime("%a").upper()


#방법2. 직접 구현
def solution(a, b):
  month_date = [31,29,31,30,31,30,31,31,30,31,30,31]            #(윤년) 2월 29일
  day_of_the_day = ['FRI','SAT','SUN','MON','TUE','WED','THU']  #1월 1일 금요일

  #1. (핵심) 1월 1일을 기준으로 주어진 날짜까지 몇 일이 지났는지 계산하기
  diff_date = 0
  #달
  for i in range(a-1):
    diff_date += month_date[i]
  #일
  diff_date += b - 1

  #요일
  return day_of_the_day[diff_date % 7]