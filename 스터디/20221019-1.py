'''
파도반 수열 문제 https://www.acmicpc.net/problem/9461
'''

'''
규칙? 전전전값 + 전전값 = 현재값
'''

'''
f(0) = 1, f(1) = 1, f(2) = 1 
n >= 3이면 f(n) = f(n-3) + f(n-2)
'''

''' 
잘못된 방법: 단순 재귀로 풀기 (시간초과)
동일한 연산을 매우 많이 수행하게 된다 (https://velog.io/@doodung/Algorithm-DP)
def recursion(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return recursion(n-3) + recursion(n-2)

T = int(input())
for _ in range(T):
  N = int(input())

  print(recursion(N-1))
'''

'''
방법: 다이나믹 프로그래밍 (보텀업 + DP테이블 사용)
DP테이블: 부분 문제의 정답을 한 번만 계산하고 저장해둔 뒤 나중에 저장해둔 정답을 이용하는 메모이제이션 기법
메모이제이션: https://www.google.com/search?q=%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98&rlz=1C1NDCM_koKR911KR911&oq=%EB%A9%94%EB%AA%A8%EC%9D%B4%EC%A0%9C%EC%9D%B4%EC%85%98&aqs=chrome..69i57j0i512l9.1993j0j15&sourceid=chrome&ie=UTF-8
dp = [0] * 100
dp[0] = 1
dp[1] = 1
dp[2] = 1

T = int(input())
for _ in range(T):
  N = int(input())

  for i in range(3,N):
    dp[i] = dp[i-3] + dp[i-2]
  
  print(dp[N-1])
'''



'''
비슷한 유형의 대표적인 피보나치 수열
https://www.google.com/search?q=%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98+%EC%88%98%EC%97%B4&rlz=1C1NDCM_koKR911KR911&oq=%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98+%EC%88%98%EC%97%B4&aqs=chrome..69i57l2j69i59j69i60j69i61l2.2215j0j15&sourceid=chrome&ie=UTF-8
규칙? 전전값 + 전값 = 현재값
f(0) = 1, f(1) = 1
n >= 2이면 f(n) = f(n-2) + f(n-1)
'''