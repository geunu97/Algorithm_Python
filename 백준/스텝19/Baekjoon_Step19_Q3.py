#19단계: 큐, 덱
#3.1번~N번까지 원을 이루고 있을 때 순서대로 K번째를 제거할 때 원에서 제거되는 순서 구하기

N,K = map(int,input().split())

q = []
for i in range(1,N+1):
    q.append(i)

answer = []
i=0
while q :
    i = (i+K-1) % len(q)    #공식
    answer.append(str(q.pop(i)))


print("<" + ", ".join(answer) + ">")



'''
0 1 2 3 4 5 6 7 

1 2   4 5 6 7   

1 2   4 5   7
1     4 5   7
'''

