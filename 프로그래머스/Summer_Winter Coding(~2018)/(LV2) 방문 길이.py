#LV2 방문 길이

def solution(dirs):
    list_a = [[0,0,0,0]]
    
    for i in dirs:
        if i == 'U':
            x = list_a[-1][2]
            y = list_a[-1][3] +1
        elif i == 'D':
            x = list_a[-1][2]
            y = list_a[-1][3] -1
        elif i == 'R':
            x = list_a[-1][2]+1
            y = list_a[-1][3]
        elif i == 'L':
            x = list_a[-1][2]-1
            y = list_a[-1][3] 
    
        if -5<=x<=5 and -5<=y<=5:
            list_a.append([list_a[-1][2],list_a[-1][3],x,y])
    
    answer = []
    for a,b,c,d in list_a:
        if [a,b,c,d] not in answer and [c,d,a,b] not in answer:
            answer.append([a,b,c,d])

    return len(answer)-1

print(solution("ULURRDLLU"))


#Point

#예외케이스 (생각 못했음..)
#방향성이 없어져야 된다. 오른쪽에서 왼쪽으로 간거하고 왼쪽에서 오른쪽으로 간거하고 결국은 같은 길이다. 