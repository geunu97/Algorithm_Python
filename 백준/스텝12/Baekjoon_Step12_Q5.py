#12단계: 정렬
#5. 하나의 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.  

list_N = list(map(int,input()))      #각 자리 자르면서 입력받기

list_N.sort()

for i in reversed(range(len(list_N))):      #내림차순 정렬
    print(list_N[i],end="")         #이어서 출력




