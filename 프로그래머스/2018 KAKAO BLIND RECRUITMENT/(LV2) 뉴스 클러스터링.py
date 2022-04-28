#LV2 뉴스 클러스터링

import math

def solution(str1, str2):
    str1_list = []
    str2_list = []
    
    for i in range(1,len(str1)):
        if str1[i-1].isalpha() and str1[i].isalpha():
            str1_list.append(str1[i-1].upper() + str1[i].upper())
        
    for i in range(1,len(str2)):
        if str2[i-1].isalpha() and str2[i].isalpha():
            str2_list.append(str2[i-1].upper() + str2[i].upper())
    
    str3_list = list(set(str1_list + str2_list))
    value1 = 0     #교집합 찾기
    value2 = 0     #합집합 찾기
    for i in str3_list:
        a = str1_list.count(i)
        b = str2_list.count(i)
        value1 += min(a,b)
        value2 += max(a,b)
        
    
    if value1 == 0 and value2 == 0:
        return 65536
    else:
        answer = math.floor(value1 / value2 * 65536)
        return answer