#3단계: for문
#3. n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

#입력조건 : 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
#출력조건 : 1부터 n까지 합을 출력한다.

a = int(input())
sum = 0

for i in range(1,a+1) :
    sum += i
print(sum)