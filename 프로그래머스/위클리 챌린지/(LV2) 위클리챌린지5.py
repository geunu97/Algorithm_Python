#LV2 모음 사전

def solution(word):
    word_list = ['A','E','I','O','U']
    number = [781,156,31,6,1]

    answer = len(word)
    for i in range(len(word)):
        answer += word_list.index(word[i]) * number[i]
    return answer


#Point
#수를 나열해서 몇개씩 있는지 찾는 문제 (약간의 노가다 필요)

#맨앞짜리를 바꾸기 위해선 781, 두번째자리 156, 세번째 자리 31, 네번째 자리 6, 마지막자리+1 필요


 