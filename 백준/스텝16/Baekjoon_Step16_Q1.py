#16단계: 그리디 알고리즘 (탐욕법)
#1. 동전 0

a,b = map(int,input().split())

list_coin = []
for i in range(a):
    input_coin = int(input())

    if input_coin > b:
        continue
    else:
        list_coin.append(input_coin)

answer = 0
for i in reversed(range(len(list_coin))):
    answer += b // list_coin[i]
    b = (b - (b // list_coin[i] * list_coin[i]))

    if b == 0:
        break

print(answer)


#각 동전이 배수의 형태를 나타내기 때문에 가장 큰 동전부터 세는 것이 맞다 (그리디)
#(시작점에서 답이 확실히 1개가 나오며, 현재 자리에서 최적의 답 1개를 구하면 전체적으로도 최적이 된다)

#DP는 시작점에서 답이 1개가 아니라 여러개를 선택해서 비교해야 하며, 현재 자리에서 최적일 지라도 전체적으로 최적이 아닐 수 있었다.
#(여러 경우의 수를 둬야 한다)