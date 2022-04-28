#10단계: 재귀
#3. (프랙탈) 별 찍기 

#프랙탈 : 작은 구조가 전체 구조와 닮은 형태로 끝없이 되풀이되는 구조

def star(num, list_a):
    if num == 3:
        list_a.append(["***"])    # [ ]로  리스트 씌여서 문자열, 공백 곱셈 및 계산
        list_a.append(["* *"])
        list_a.append(["***"])
        return list_a
    else:
        b = star(num//3,list_a)*3

        for i in range(len(b)):
            if i in list(range(num//3,num-num//3)):
                b[i] = b[i] + [" "]*(num//3) + b[i]
            else:
                b[i] = b[i]*3
        return b

list_a=[]

N = int(input())

a = star(N,list_a)

for i in range(len(a)):
    print("".join(a[i]))    # 한칸씩 (이중리스트) join함수로 연결해서 출력하기




