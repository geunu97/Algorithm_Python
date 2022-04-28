#LV2 H-Index

def solution(citations):
    answer = 0
    citations = sorted(citations)[::-1]
    for index in range(len(citations)):
        if index + 1 <= citations[index]:
            answer = index+1
        else:
            return answer
    
    return answer
        