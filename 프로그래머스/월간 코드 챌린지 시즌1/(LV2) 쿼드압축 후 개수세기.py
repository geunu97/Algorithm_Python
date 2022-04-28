#LV2 쿼드압축 후 개수세기

def solution(arr):
    answer = [0,0]    # [0의 개수, 1의 개수]
    len_value = len(arr)
    
    def comp(x,y,len_value):
        init = arr[x][y]
        for i in range(x, x+len_value):
            for j in range(y, y+len_value):
                if arr[i][j] != init:    
                    nn = len_value//2       # wow...
                    comp(x, y, nn)
                    comp(x+nn, y, nn)
                    comp(x, y+nn, nn)
                    comp(x+nn, y+nn, nn)
                    return
    
        answer[init] += 1
    
    comp(0,0,len_value)
    
    return answer

#재귀