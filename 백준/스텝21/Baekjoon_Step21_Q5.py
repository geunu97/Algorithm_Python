#15단계: 이분 탐색(이진 탐색)
#5. n*n크기의 2차원 A리스트에서 안에 있는 수는 A[i][j] = i*j로 되어있다. 이 수들을 일차원 B리스트에 오름차순으로 넣을 때 B[k]를 구하기  (인덱스는 1부터 시작)

n = int(input())
k = int(input())

start = 1    #시작값은 어떤 특정값의 최솟값으로 설정(인덱스)
end = k      #끝값은 어떤 특정값의 최댓값으로 설정(인덱스)

answer = 0
while start <= end:
    mid_value = (start + end)//2
    count = 0

    for i in range(1, n+1):      #특정값 mid_value보다 작거나 같은 수가 몇개 있는지 구하기, 1~n행까지 각 행별로  (특정값 // 각 행) 나눠서 모두 더하기
        count += min(n, mid_value//i)      

    if count < k:
        start = mid_value + 1
    else:
        answer = mid_value
        end = mid_value - 1

print(answer)

#Point
#어떤 특정값을 탐색값으로 설정하고 그 특정값까지의 개수가 K개라면 B[k]를 구할 수 있다(k번째 인덱스를 알 수 있다)
#                                   ->특정값까지의 개수는 1~n헹까지 각행씩 (특정값 // 각 행) 나눠서 모두 더하면 구할 수 있다

#ex)특정값까지의 개수 구할 때 // 특정값(mid_value)이 3이라면 // 3까지의 작거나 같은 수의 갯수 구할 때
#1 2 3         (3 // 1)  3개
#2 4 6    ->   (3 // 2)  1개    -> 5개
#3 6 9         (3 // 3)  1개 
 