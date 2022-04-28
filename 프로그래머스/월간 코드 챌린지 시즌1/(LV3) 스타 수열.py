#LV3 스타 수열

def solv(list_a):        
    if (list_a.count(list_a[0]) == len(list_a) // 2) or (list_a.count(list_a[1]) == len(list_a) // 2):
        return True
    else:
        return False
        
def solution(a):
    dp = [0] * (len(a)+1)
    
    for i in range(2,len(a)+1,2):
        if a[i-1] != a[i]:
            if solv(a[:i]):
                dp[i] = dp[i-2] + 2
            else:
                dp[i] = dp[i-2]
        else:
            dp[i] = dp[i-2]
        
    return dp[-1]


#?????????????


#그냥 다시 거꾸로 카카오부터 풀까!???
