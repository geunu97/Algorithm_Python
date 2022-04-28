#LV1 완주하지 못한 선수

def solution(participant, completion):
    dictionary = {}
    for i in participant:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    
    for i in completion:
        dictionary[i] -= 1
    
    for key in dictionary:
        if dictionary[key] == 1:
            return key


#Point
#해쉬 문제