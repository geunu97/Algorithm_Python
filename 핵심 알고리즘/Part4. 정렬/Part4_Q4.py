#Part4. 정렬
#문제 4. 이름과 국어, 영어, 수학 점수가 주어질 때 // 
#        국어가 감소하는 순, 국어가 같으면 영어가 증가하는 순, 영어가 같으면 수학이 감소하는 순, 수학이 같으면 이름이 증가하는 순으로 정렬하기

N = int(input())
list_a = []
for i in range(N):
  a,b,c,d = input().split()
  list_a.append([a,int(b),int(c),int(d)])

list_a = sorted(list_a,key = lambda x: (-x[1],x[2],-x[3],x[0]))  

for a,b,c,d in list_a:
  print(a)

#a를 내림차순으로 a가 같을때 b를 오름차순으로 b가 같을 때 c를 내림차순으로 c가 같을 때 d를 오름차 순으로 정렬하기!!!!   -붙이기!!!!!!!!!

#이름만 출력하기 

