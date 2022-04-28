#14단계: 백트래킹
#6. 

'''
list_a=[]
list_sudoku=[]

for i in range(9):
    list_a = list(map(int,input().split()))
    list_sudoku.append(list_a)

def re():

    #가로 검사
    for i in range(9):
        list_1_9 = [1,2,3,4,5,6,7,8,9]

        if list_sudoku[i].count(0) == 1:
            number_list = list(set(list_1_9) - set(list_sudoku[i]))
            number = number_list[0]

            for j in range(9):
                if list_sudoku[i][j] == 0:
                    list_sudoku[i][j] = number
                    break

    #세로 검사
    for i in range(9):
        list_1_9 = [1,2,3,4,5,6,7,8,9]
        count = 0

        for j in range(9):
            if list_sudoku[j][i] == 0:
                index_j = j
                index_i = i
                count += 1

        if count == 1 :
            new_list = []
            for k in range(9):
                if list_sudoku[k][i] != 0:
                    new_list.append(list_sudoku[k][i])
            
            number_list = list(set(list_1_9) - set(new_list))
            number = number_list[0]
            list_sudoku[index_j][index_i] = number 

    #3*3 검사
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3):
        for j in range(3):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #두번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3):
        for j in range(3,6):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #세번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3):
        for j in range(6,9):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #네번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3,6):
        for j in range(3):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #다섯번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3,6):
        for j in range(3,6):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #여섯번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(3,6):
        for j in range(6,9):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #일곱번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(6,9):
        for j in range(3):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number


    #여덟번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(6,9):
        for j in range(3,6):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number

    #아홉번째 3*3
    list_1_9 = [1,2,3,4,5,6,7,8,9]
    new_list=[]
    for i in range(6,9):
        for j in range(6,9):
            new_list.append(list_sudoku[i][j])

            if list_sudoku[i][j] == 0:
                index_i = i
                index_j = j

    if 0 in new_list:
        number_list = list(set(list_1_9) - set(new_list))
        number = number_list[0]
        list_sudoku[index_i][index_j] = number


    if list_sudoku.count(0) > 0:
        re()
    else:
        for x in range(9):
            for y in range(9):
                print(list_sudoku[x][y],end=" ")
            print("")
        return

re()
'''
#가로검사
#세로검사
#3*3검사

#파이썬 시간초과...!







'''
list_a = [1,2,3]
list_b = [1,2,0]
number_list = list(set(list_a) - set(list_b))  # 꼭 표현 알아놓기!!!!!   ,딕셔너리로 변환 -> 리스트 변환
number = number_list[0]
print(number)
'''



