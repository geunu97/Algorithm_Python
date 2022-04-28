#8단계: 기본 수학 1
#3. 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.
'''
1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
'''
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 
# 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

a = int(input())

aa = a

while True:

    if aa == 1 :
        print("1/1")
        break

    for k in range(1,5000):
        if (k*k + k) / 2 < aa <= ((k+1)*(k+1) + (k+1)) / 2 :
            stop_k = k+1
            break

    if stop_k % 2 != 0:
        number_1 = aa - (k*k + k) / 2 

        i = int(stop_k - number_1 +1)
        j = int(number_1)

        print("%d/%d"%(i,j))
        break

    elif stop_k % 2 == 0:
        number_1 = aa - (k*k + k) / 2

        i = int(number_1)
        j = int(stop_k - number_1 + 1)

        print("%d/%d"%(i,j))
        break



#규칙 찾기   # 1  3  6  10   #계차수열    #  (n*n + n) / 2   #일반항 구하기  

'''
1/1

1/2
2/1

3/1
2/2
1/3

1/4
2/3
3/2
4/1

5/1
4/2
3/3
2/4
1/5
'''
