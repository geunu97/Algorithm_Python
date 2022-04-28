#LV2 영어 끝말잇기
#1번~n번까지 n명의 사람이 영어 끝말잇기를 하고 있다
#1번 부터 진행하며 n번이 끝난 후에 다시 1번부터 쭉 진행한다
#이전에 등장했던 단어는 사용할 수 없고, 한 글자인 단어는 인정되지 않는다

#이 때 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지 구하기

import math

def solution(n, words):
    if len(words[0]) == 1:
        return [1,1]
        
    clear = 0
    for i in range(1,len(words)):
        if len(words[i])== 1:
            clear = 0
            break

        if words[i-1][-1] == words[i][0]:
            if words[i] in words[:i]:
                clear = 0
                break
            else:
                clear = 1
                continue
                
        if words[i-1][-1] != words[i][0]:
            clear = 0
            break
    
    if clear == 0:
        if (i+1) % n == 0:
            value = n
        else:
            value = (i+1) % n
        return [value, math.ceil((i+1)/n)]
                
    if clear == 1:
        return [0,0]


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))