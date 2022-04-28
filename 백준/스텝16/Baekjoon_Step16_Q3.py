#16단계: 그리디 알고리즘 (탐욕법)
#3. 줄 순서
  
a= int(input())

list_a = list(map(int,input().split()))

list_a = sorted(list_a)

sum = 0
sum2 = 0
for i in range(a):
    sum =  sum + list_a[i]
    sum2 += sum

print(sum2)