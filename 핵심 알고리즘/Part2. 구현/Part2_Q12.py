#Part2. 구현
#문제 12. 외벽점검

#pass..
''' 
def solution(n, weak, dist):
    list_a = [0]*n
    for i in weak:
        list_a[i] = 1

    dx = [1,-1]  #오른쪽 왼쪽으로만 이동
    looks = [0,1] #바라보는 방향
    first_dist_len = len(dist)

    list_a = tuple(list_a)    #매우 중요!!!!!!!!
    
    for _ in range(len(dist)):
        dist_value = dist[-1]
        max_value = -987654321

        for i in range(n):          #시물레이션 시작
            for look in looks:
                list_b = list(list_a)

                x = i  #시작점
                list_b[x] = 0  
                for _ in range(dist_value):
                    nx = x + dx[look]
                    
                    if nx < 0 :                #원형리스트
                        nx = len(list_a)-1

                    if nx > len(list_a)-1:
                        nx = 0
                        
                    list_b[nx] = 0
                    x = nx   #현재 위치 리셋!!!
 
                count_value = list_b.count(0)

                if max_value < count_value:  #and ?? 남은 애들 거리가 좁은애들도? 
                    max_value = count_value
                    look_value = look
                    index_value = i
                print(i,look,list(list_b),look_value,index_value,count_value)
           
        list_a = list(list_a)
        x = index_value
        list_a[x] = 0
        for _ in range(dist_value):
            nx = x + dx[look_value]
            list_a[nx] = 0

            x = nx
        print(list(list_a))

        list_a=tuple(list_a)
        dist.pop()

        if 1 not in list(list_a):
            print(first_dist_len - len(dist))
            exit()
            #return first_dist_len - len(dist)



solution(12, [1,5,6,10], [1,2,3,4])
'''