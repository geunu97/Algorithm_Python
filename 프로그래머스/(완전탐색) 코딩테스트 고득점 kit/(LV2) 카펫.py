#LV2 카펫

def solution(brown, yellow):
    list_a = []
    for i in range(1,yellow+1):   
        if yellow % i == 0:       #yellow 약수구하기
            value = yellow // i
            if value >= i:        #가로의 크기가 같거나 클 때만
                list_a.append([value,i])
    
    for m,n in list_a:
        result = m*2 + n*2 + 4    #테두리 갯수
        if result == brown:
            return [m+2,n+2]