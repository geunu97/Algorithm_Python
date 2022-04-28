#Part6. 다이나믹 프로그래밍(DP)
#문제 9. 19번과 비슷한 문제, 문자열 A를 문자열 B로 만들려고 할 때 최소 연산의 횟수 구하기 (조건 1.삽입 2.삭제 3.교체) 
#        (ex) sunday saturday 답은 3)

word1 = input()
word2 = input()

dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]  

for i in range(1, len(word1)+1):   
    dp[i][0] = i
    
for j in range(1, len(word2)+1):   
    dp[0][j] = j

for i in range(1, len(word1)+1): 
    for j in range(1, len(word2)+1): 
        if word1[i-1] == word2[j-1]:  #두 문자가 같을 때
            dp[i][j] = dp[i-1][j-1]
        else:          #두 문자가 다를 때
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[len(word1)][len(word2)])   #마지막 인덱스 값 확인


#Point
#2차원 형태로 그려서 풀기 (노트에 그려놓기)
                

#식 만들기
#1. 두 문자가 같을 때 : dp[i][j] = dp[i-1][j-1]
#2. 두 문자가 다를 때 : dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])  // (삽입:왼쪽 , 삭제:위쪽 , 교체:왼쪽 위) 중에서 가장 작은 수 + 1

