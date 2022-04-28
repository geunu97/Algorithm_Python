#15단계: 이분 탐색(이진 탐색)
#3. 랜선 자르기, 자르는 길이를 정해서 서로다른 여러개 랜선들 잘라서 같은 길이로 n개이상 만들기 (자르는길이를 140으로 했을 때 300을 자르면 2개가 된다)
#   자르는 길이 최댓값 구하기

k, n = map(int, input().split())
list_a = []
for i in range(k):
    list_a.append(int(input()))

list_a = sorted(list_a)

start = 1         #시작값 자르는길이 최솟값 1로 설정
end = list_a[-1]   #끝값 자르는길이 최댓값으로 설정

result = 0
while start <= end:
    mid_value = (start + end) // 2
    count = 0   

    for i in list_a:
        count += i // mid_value    #자른 후 갯수 더해주기

    if count >= n:
        result = mid_value
        start = mid_value + 1
    else:
        end = mid_value - 1

print(result)

#자르는 길이를 탐색값으로 설정

