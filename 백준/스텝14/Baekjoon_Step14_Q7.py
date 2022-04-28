#14단계: 백트래킹
#7. 연산자 끼워넣기 (삼성 SW 역량 테스트 기출 문제 1)

# 숫자의 위치는 그대로, 사이에 연산자 끼워 넣을 수 있는 방법으로 모두 끼워 넣어서 최대, 최댓값 최소값 찾기


N = int(input())

list_a = list(map(int,input().split()))   #수

list_b = list(map(int,input().split()))   #연산자

max_num = -1000000001
min_num = 1000000001

def DFS(count,number,plus,minus,mul,div):
    global max_num
    global min_num             #함수 안에서 밖에 있는 변수 사용하기

    if count == N:   #길이 맞으면(최종 계산 끝나면) 값 넣기
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
        return
    
    #각각 시작점 정하는 단계(모두 따짐)
    if plus:                     #0이 아니면 모두 True기 때문
        DFS(count+1,number + list_a[count],plus-1,minus,mul,div)
    if minus:                   #위에 plus조건 모두 끝나면 처음부터 다시 minus조건부터 시작  
        DFS(count+1,number - list_a[count],plus,minus-1,mul,div)
    if mul:
        DFS(count+1,number * list_a[count],plus,minus,mul-1,div)          
    if div:
        DFS(count+1, int(number/list_a[count]) ,plus,minus,mul,div-1)


DFS(1,list_a[0],list_b[0],list_b[1],list_b[2],list_b[3])
print(max_num)
print(min_num)


#첫 수부터 계산시작

#Point
#DFS (당연히 재귀로 구현하는 문제)
#재귀로 연산자 들어갈 수 있는 모든 방법 => 각각 시작점 다르게 정해서 재귀로 구현!!!!!! (시작점 각각 정해서 재귀함수 넣는게 가장 중요)
#연산자의 갯수 조건에 맞으면 최종값 출력하고 최대값, 최소값 비교해서 넣기
#맨 앞에 수 부터 순서대로 계산하기!
