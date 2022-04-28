#LV2 방금그곡

def replace_(str):    #replace사용하기
    str = str.replace('C#','c')
    str = str.replace('D#','d')
    str = str.replace('F#','f')
    str = str.replace('G#','g')
    str = str.replace('A#','a')
    
    return str

def solution(m, musicinfos):
    answer = []
    
    m = replace_(m)
    
    for i in musicinfos:  #한세트씩 불러오기
        i = i.split(',')      #split사용해서 나누기
        
        hour = int(i[1][:2]) - int(i[0][:2])      #시간 빼기해서 구하기
        minute = int(i[1][3:5]) - int(i[0][3:5])   
        
        time = hour * 60 + minute   #분으로 바꾸기
        
        i[3] = replace_(i[3])
        
        result = ""  
        j = 0
        while True:   #time길이 맞춰서 문자 하나씩 넣기
            if time == len(result):
                break
            
            result += i[3][j]
            j += 1
            
            if j == len(i[3]):
                j = 0
            
        #print(m)
        #print(result)
        if m in result:    #리스트말고 문자열로 해야, 문자열이 포함되어 있는지 in사용해서 구할 수 있음 
            answer.append([time,i[2]])

            
    if len(answer) == 0:
        return '(None)'
    
    else:
        answer = sorted(answer, key = lambda x: (-x[0]))      #시간 내림차순 정렬
        return answer[0][1]



#Point
# replace 사용하기
# #이 들어간 것을 모두 똑같이 한자리 문자로 다르게 바꿔줘야댐 //   그렇게 안하면 길이 등 조건 맞추기 아주 까다로움     



#어려웠던 문제!!!
#노트에 꼭 써놓기!!! 