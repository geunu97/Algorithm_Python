#LV3 숫자게임
#A팀 B팀으로 나누어서 각자 서로의 수를 비교할 때, 큰 수를 가진쪽이 이기며 이길때만 승점1점을 얻는다.
#A팀의 출전순서와 수가 정해졌을 때, B팀은 그것을 보고 출전 순서를 정해 최종 승점을 가장 높게 구해라

def solution(A, B):
    answer = 0
    A.sort()      #A를 내림차순 정렬, B를 내림차순 정렬
    A.reverse()
    B.sort()
    B.reverse()     
    
    while B:
        if B and B[-1]>A[-1]:
            answer+=1
            A.pop()
        B.pop()
    
    return answer


print(solution([5,1,3,7],[2,2,6,8]))


#Point

#     B승                         B승        B승              
#A [7,5,3,1]    -> [7,5,3]  ->  [7,5,3]  -> [7,5]  -> [7]  
#B [8,6,2,2]       [8,6,2]      [8,6]       [8]