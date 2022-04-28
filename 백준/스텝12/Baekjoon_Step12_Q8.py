#12단계: 정렬
#8. 단어 정렬

N = int(input())

list_a=[]                
list_list = []
for i in range(N):
    a = input()
    b = len(a)

    if a in list_list:       #set() 사용해도 됨 - set()의 특징은 중복제거 한 후 순서가 뒤죽박죽 되기 때문에 list(set())처럼 list로 감싸줘야함
        continue                                # 단순하게 set()만 사용하게 되면 리스트의 인덱스에 접근할 수 없다
    else:
        list_list.append(a)
        list_a.append([a,b])
        
list_a = sorted(list_a,key = lambda x: (x[1],x[0]))

for i in range(len(list_a)):
    print(list_a[i][0])






