#8단계: 기본 수학 1
#5번 문제

a = int(input())

for i in range(a):
    h,w,n = map(int,input().split())

    Y = n % h 

    X = n // h + 1

    if Y == 0:
        Y = str(h)
        X = X - 1
        X = str("{:02d}".format(X))
    else:
        Y = str(Y)
        X = str("{:02d}".format(X))
   
    print(Y+X)
    #print("%d%02d"%(X,Y)) 출력형태 2번째 방법



  

