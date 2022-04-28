#14단계: 백트래킹
#2. 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#   고른 수열은 오름차순이어야 한다.

N,M = map(int,input().split())

list_a=[]
def DFS(start):
    if len(list_a) == M:
        print(" ".join(map(str,list_a)))
        return

    for i in range(start,N+1):
        if i not in list_a: 
                list_a.append(i)
                DFS(i+1)
                list_a.pop()

DFS(1)