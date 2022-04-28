#LV2 n진수 게임

def calc(a,n):
    list_a = ['0']
    for i in range(1,a):
        list_b = []
        while True:
            value = i % n
            if value == 10:
                list_b.append('A')
            elif value == 11:
                list_b.append('B')
            elif value == 12:
                list_b.append('C')            
            elif value == 13:
                list_b.append('D')            
            elif value == 14:
                list_b.append('E')            
            elif value == 15:
                list_b.append('F')
            else:
                list_b.append(value)
        
            i = i // n
        
            if i == 0:    #0이면 종료!
                break
                
        for j in reversed(range(len(list_b))):    #n진법 만들때 숫자가 거꾸로 만들어져서 원래대로 해줘야댐
            list_a.append(str(list_b[j]))

    return list_a
    #print(list_a)

def solution(n, t, m, p):
    a = m * t  #최대
    
    result_list = calc(a,n)
        
    result = ""
    for i in range(p,a+1,m):
        result += result_list[i-1]
    
    return result


#숫자 0부터 쭉 차례대로 숫자들을 n진법으로 바꿔서 표현하고, 총 m명이서 게임하며 한명이 p순서일 때마다 총t번 말할때까지 한다
