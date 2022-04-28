#14단계: 백트래킹
#1. 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.  (DFS문제)
#   1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 

n,m = map(int,input().split())
 
list_a = []
 
def DFS():
    if len(list_a)==m: 
        print(' '.join(map(str,list_a)))
        return
    
    for i in range(1,n+1):
        if i not in list_a: 
            list_a.append(i) 
            DFS()
            list_a.pop()   #마지막 요소 제거
 
DFS()


#재귀함수 사용 -> DFS
#1부터 N까지 M개씩 모두 탐색하기