#15단계: 이분 탐색(이진 탐색)
#6.(LIS)최장 증가 부분 수열 (LIS : Longest Increasing Subsequence) 가장 긴 증가하는 부분 수열2, 가장 긴 증가하는 부분 수열 길이 구하기
#ex) 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.


from bisect import bisect_left 

a = input()
list_a = list(map(int, input().split()))
dp = []

for i in list_a: #for문으로 리스트 앞부터 모두 보기 (하나씩 따져서 새로운 리스트에 값 넣기)
    k = bisect_left(dp, i) #자신이 삽입될 인덱스 k  
    if len(dp) <= k:  #현재 값이 수열에서 가장 크다면
        dp.append(i)
    else:
        dp[k] = i #같은 수일 때는 같은 수와 또는 자신보다 바로 뒤에 있는 큰 수와 값 바꾸기
print(len(dp))

#Point
#이 문제는 이분탐색으로 풀면 길이는 맞출 수 있지만 정확한 수열을 도출할 수는 없다.
#ex) list_a = 3 5 7 9 2 1 4 8 일 때 여기 답으로는 3 5 7 9 이지만 실제로는 1 4 7 8로 나온다



