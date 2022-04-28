#12단계: 정렬
#10. 좌표 압축

import sys
input = sys.stdin.readline

N = int(input())

list_a = list(map(int,input().split()))
list_list = list_a         #2 4 -10 4 -9

list_a = set(list_a)       #2 4 -10 -9

list_a = sorted(list_a)    #-10 -9 2 4

dictionary = { }
k = 0
for i in list_a:                      #리스트 X , 딕셔너리로 하는 이유 => 해당 키 값에 대응하는 value값을 출력해야 하기 때문에 
    dictionary[i] = k                 
    k += 1

for j in list_list:                   #반목문 리스트로 돌리기!!
    print(dictionary[j],end=" ")       


#Point
#자신의 수와 나머지 수들 모두 비교하는게 아니라 중복제거 후
#정렬한 후 각 인덱스 위치가 그 값이 됨 (계산횟수 적게 든다)

