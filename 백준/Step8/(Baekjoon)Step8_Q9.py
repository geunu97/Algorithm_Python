#8단계: 기본 수학 1
#9번 문제

import math

a = int(input())

for i in range(a):
  x,y=map(int,input().split())

  n = y-x-1
  n_sqrt = math.sqrt(n)
  n_sqrt = int(n_sqrt)

  if n_sqrt * (n_sqrt + 1) > n:                        
    answer = 2 * n_sqrt -1

  elif  n_sqrt * (n_sqrt + 1) <= n:
    answer = 2 * n_sqrt 

  print(answer+1)



#1 * 2  //  2 * 3  // 3 * 4  //  4 * 5 


# 2 3    4 5    6 7 8    9 10 11     12 13 14 15   16 17 18 19
#  2      3       4         5             6             7


 #y-x-1!!!!     # 마지막은 +1해주기
 #마지막에 1이 나올라면 전에 2, 1, 0 이 나와야 함
 #최소로 도달
 #처음은 무조건 1
 #반목문 돌리면 안됨


'''
 2 3    4 5    6 7 8    9 10 11     12 13 14 15   16 17 18 19
  2      3       4         5             6             7


2   1 1
3   1 2

4   1 2 1
5   1 2 2

6   1 2 2 1
7   1 2 2 2
8   1 2 3 2

9   1 2 3 2 1
10  1 2 3 2 2
11  1 2 3 3 2

12  1 2 3 3 2 1
13  1 2 3 3 2 2
14  1 2 3 3 3 2
15  1 2 3 4 3 2

16  1 2 3 4 3 2 1
'''
   


 
