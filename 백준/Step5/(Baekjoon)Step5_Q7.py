#5단계: 1차원 배열
#7. 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

a = int(input())

sum = 0
count = 0

for i in range(a):
    list_a = list(map(float,input().split()))

    for j in range(1,len(list_a)):
        sum += list_a[j]

    avg = float(sum / (len(list_a)-1))

    for k in range(1,len(list_a)):
        if list_a[k] > avg :
            count += 1 

    answer = float(count / list_a[0] * 100)

    print("{:.3f}%".format(answer))

    list_a.clear()
    sum = 0
    count = 0

