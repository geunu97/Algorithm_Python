#LV2 피로도
# k라는 피로도를 사용해서 던전을 탐험할 때, 
# [최소 필요 피로도,소모 피로도]가 있을 때 던전 하나당  k가 최소필요피로도보다 같거나 커야 지나갈 수 있으며 지나간 후에 k피로도에서 소모피로도만큼 뺀다 
# 최대 몇개의 던전을 지나갈 수 있는지 구하기 (어떤 던전부터 가야하는지에 따라 달라진다)

from itertools import permutations

def solv(dungeon,kk,count):
    for a,b in dungeon:
        if kk >= a:
            kk -= b
            count += 1
        else:
            break
    return count

def solution(k, dungeons):
        
    teams = list(permutations(dungeons,len(dungeons)))
    
    answer = []
    for i in teams:
        answer.append(solv(i,k,0))

    return max(answer)

print(solution(80,[[80,20],[50,40],[30,10]] ))

#Point
#조합으로 푸는 문제!! 