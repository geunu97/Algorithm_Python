#Part4. 정렬
#문제 3. 같은 길이의 2개의 리스트를 입력받아서 K번 바꿔치기 해서 A리스트의 합 최대로 만들기
#        바꿔치기란 a의 원소 1개와 b의 1원소를 바꾸는 것을 말한다  (A의 최솟값이랑 B의 최댓값이랑 바꾸면 된다)

N,k = map(int,input().split())

list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

list_a = sorted(list_a)
list_b = sorted(list_b)
list_b.reverse()

for i in range(3):
  list_a[i] = list_b[i]

print(sum(list_a))