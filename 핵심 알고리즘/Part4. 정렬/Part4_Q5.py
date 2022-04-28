#Part4. 정렬
#문제 5. 안테나 1개 설치하려는데 안테나로부터 모든 집 까지의 거리의 합이 최소가 되도록 안테나 위치 구하기 

N = int(input())

list_a = list(map(int,input().split()))

list_a = sorted(list_a)

if len(list_a) % 2 == 0:   #길이가 짝수일 때
    number = len(list_a) // 2 - 1
else:                      #길이가 홀수일 때
    number = len(list_a) // 2

print(list_a[number])


#가운데 값 찾으면 됨


