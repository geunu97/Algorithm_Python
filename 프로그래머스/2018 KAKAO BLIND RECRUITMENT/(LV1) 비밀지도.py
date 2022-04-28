#LV1 비밀지도

def solution(n, arr1, arr2):
    list_a = []
    list_b = []

    for i in arr1:
        bin_value = "{:b}".format(i)   #2진법변환
        
        if len(bin_value) != n:
            len_value = n - len(bin_value)
            bin_str = ("0" * len_value) + str(bin_value)       #길이 맞추기
            list_a.append(bin_str)
        else:
            list_a.append(str(bin_value))      #다른숫자들과 비교시 이진법은 문자열로 변환해서해야 좋음
            
        
    for i in arr2:
        bin_value = "{:b}".format(i)
        
        if len(bin_value) != n:
            len_value = n - len(bin_value)
            bin_str = ("0" * len_value) + str(bin_value)
            list_b.append(bin_str)
            
        else:
            list_b.append(str(bin_value))
    
    answer = []
    for i in range(n):
        result = ""     #출력 형식 맞추기 위해
        for j in range(n):
            if list_a[i][j] != list_b[i][j]:
                result += '#'
            elif list_a[i][j] == list_b[i][j] and list_a[i][j] == '1':
                result += '#'
            elif list_a[i][j] == list_b[i][j] and list_a[i][j] == '0':
                result += ' '
        
        answer.append(result)
    
    return answer