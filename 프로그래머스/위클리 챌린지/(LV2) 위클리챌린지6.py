def solution(line):

    #교점이 평행하거나 일치해서 없을 때 // 교점이 하나일 때 둘 다 문제에서 지정해준 공식으로 풀면 됨
    result = []
    for i in range(0,len(line)-1):
        for j in range(1,len(line)):
            if line[i][0] * line[j][1] - line[i][1] * line[j][0] == 0:
                continue
            else:
                x = ((line[i][1] * line[j][2]) - (line[i][2] * line[j][1])) / ((line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))
                y = ((line[i][2] * line[j][0]) - (line[i][0] * line[j][2])) / ((line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))
                result.append([x,y]) 
    
    # 1.0 , 1.2 같은 float자료형에서 소수점자리가 0인 경우 정수인지 실수인지 판별하는 법
    result2 = []
    for a,b in result:
        if a.is_integer() and b.is_integer():
            if [int(a),int(b)] not in result2:
                result2.append([int(a),int(b)])
    
    #최소,최대로 나올 수 있는 수가 10^15까지 , 그래서 더 크게 잡아줘야 한다
    #별이 있는 구간만 구하기 위해서 구하는 것, x축의 최소-최대 , y축의 최소-최대
    min_x = 99999999999999
    max_x = -99999999999999
    min_y = 99999999999999
    max_y = -99999999999999
    for a,b in result2:
        if min_x > a:
            min_x = a
        if max_x < a:
            max_x = a
        
        if min_y > b:
            min_y = b
        if max_y < b:
            max_y = b
    answer = [["."] * (max_x-min_x+1) for _ in range(max_y-min_y+1)]   #별이 있는 최대 구간 지정
    
    #x축,y축의 좌표값을 -> 인덱스에 맞춰서 '*' 넣어주기!! 중요!!!
    #좌표에서는 [0,0]이 한 가운데에 있기 때문에, 인덱스로 나타내기 쉽지 않다 (아래처럼 넣어주면 된다)
    for x,y in result2:
        answer[max_y - y][x - min_x] = "*"
        
    
    return [''.join(ans) for ans in answer]  #2차원 배열 -> 일차원 문자열 배열로 답 구하기


  #노트에 써놓기