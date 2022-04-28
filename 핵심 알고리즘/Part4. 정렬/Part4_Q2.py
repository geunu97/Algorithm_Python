#Part4. 정렬
#문제 2. 이름과 점수가 주어질 때, 점수가 낮은 순대로 정렬하여 이름만 출력하기
#2                
#홍길동 95
#이순신 77

#이순신 홍길동


N = int(input())

list_a = []
for i in range(N):
  a,b = input().split()
  list_a.append([a,int(b)])

list_a = sorted(list_a,key = lambda x: x[1])

for x,y in list_a:
  print(x,end=" ")