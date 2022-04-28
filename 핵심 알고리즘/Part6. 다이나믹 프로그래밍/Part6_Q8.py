#Part6. 다이나믹 프로그래밍(DP)
#문제 8. 못생긴 수

n = int(input())

dp = [0] * 1001

count = 1
for i in range(2,1001):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        count += 1 
    if count == n:
        print(i)
        break


#