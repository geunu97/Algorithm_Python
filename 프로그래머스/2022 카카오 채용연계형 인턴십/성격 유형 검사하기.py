dictionary = {
    'R': 0,
    'T': 0,
    'C': 0,
    'F': 0,
    'J': 0,
    'M': 0,
    'A': 0,
    'N': 0
}

def calc(word1,word2):
    if dictionary[word1] > dictionary[word2]:
        return word1
    elif dictionary[word1] < dictionary[word2]:
        return word2
    else:
        if word1 > word2:
            return word2
        else:
            return word1
    
def solution(survey, choices):
    for index in range(len(survey)):
        score = choices[index] - 4
        if score > 0:
            dictionary[survey[index][1]] += score
        elif score < 0:
            dictionary[survey[index][0]] += -score
    
    answer = ""
    answer += calc('R','T')
    answer += calc('C','F')
    answer += calc('J','M')
    answer += calc('A','N')
    
    return answer
