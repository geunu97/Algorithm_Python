#LV1 숫자 문자열과 영단어

def solution(s):
    list_a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    result = ''
    search = ''
    for i in s:
        if i.isalpha():
            search += i
            if search not in list_a:
                continue
            else:
                result += str(list_a.index(search))
                search = ''

        else:
            result += i
    
    return int(result)

print(solution("one4seveneight"))