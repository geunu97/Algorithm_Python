#6단계: 함수
#3. 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
#   N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

a = int(input())

def solve(num):
    if num < 100 :
        count = num
        return count
    elif num == 1000:
        return 144
    else:
        num_1 = num % 10
        num_10 = num % 100 // 10
        num_100 = num % 1000 // 100

        count = 0

        if (num_100 - num_10) == (num_10 - num_1):
            count += 1
        return count

num_count = 99

if 100 <= a < 1000 :
    for i in range(100,a+1):
        num_count += solve(i)
    print(num_count)
else:
    print(solve(a))


