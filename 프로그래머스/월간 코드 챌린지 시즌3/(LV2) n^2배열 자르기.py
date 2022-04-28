#LV2 n^2배열 자르기

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(i//n,i%n) +1)
    
    return answer


'''
n이 3일 때
1 2 3             1 2 3  2 2 3  3 3 3
2 2 3
3 3 3

n이 4일 때
1 2 3 4           1 2 3 4  2 2 3 4  3 3 3 4  4 4 4 4
2 2 3 4
3 3 3 4
4 4 4 4
'''


#Point
# (몫 vs 나머지) 최댓값




