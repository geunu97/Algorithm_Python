#14단계: 백트래킹
#3. 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#   1부터 N까지 자연수 중에서 M개를 고른 수열
#   같은 수를 여러 번 골라도 된다.

N,M = map(int,input().split())

list_a=[]
def DFS():
    if len(list_a) == M:
        print(" ".join(map(str,list_a)))
        return
    
    for i in range(1,N+1):
        list_a.append(i)
        DFS()
        list_a.pop()

DFS()


#DFS 자기 자신의 수 포함하는 문제