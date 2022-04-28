#15단계: 동적 계획법1 (DP 다이나믹프로그래밍)
#14. LCS (Longest Common Subsequence, 최장 공통 부분 수열)
#    두 문자가 주어졌을 때, 두 문자의 공통 부분중 가장 긴 길이 구하기   (ex) ACAYKP와 CAPCAK의 LCS는 ACAK가 된다)

word1 = input() 
word2 = input()

dp = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]

for i in range(1, len(word2)+1):
    for j in range(1, len(word1)+1):
        if word2[i-1] == word1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
print( dp[len(word2)][len(word1)] )



