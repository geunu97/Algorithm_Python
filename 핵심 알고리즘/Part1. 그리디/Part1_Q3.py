#Part1. 그리디
#문제 3. 주어진 n을 1이 될 때까지 나누는데 (조건1. n을 k로 나눠질때만 n을k로 나눌 수 있다.  조건2. n에서 1을 뺀다 )
#        최소 횟수 구하기
  
n,k = map(int,input().split())

def re(n,count):
  if n == 1 :
    return count
  elif n % k == 0:
    n = n // k
    count += 1
    return re(n,count)
  else:
    n = n - 1
    count += 1
    return re(n,count)

print(re(n,0))

#K가 2이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있다.