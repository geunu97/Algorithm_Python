#LV2 후보키

from itertools import combinations

def solution(relations):
    key_index = []   #인덱스로 초기화
    for i in range(len(relations[0])):
        key_index.append(i)
    
    answer = []
    count = 1       #조합요소 1개부터 늘려가면서 계산
    while True:
        for com in list(combinations(key_index, count)):
            dictionary = {}

            for relation in relations:            
                key_value = ""
                for co in com:
                    key_value += (relation[co]+' ')   #여러개의 인덱스 조합일 경우, 문자열로 이어붙였다

                if key_value not in dictionary:
                    dictionary[key_value] = 1
            
            #유일성 검사
            if len(relations) == len(dictionary):
                #최소성 검사
                check = 1
                for ans in answer:
                    check2 = 0
                    for an in ans:
                        if an in com:
                            check2 += 1
                    if check2 == len(ans):
                        check = 0
                if check == 1:
                    answer.append(com)
                
        count += 1
        if count == len(relations[0])+1:
            break

            
    return len(answer)

'''
#주의1 
1. 최소성이 되어야한다는 뜻은 ["학번"]도 후보키가 될 수있고, ["학번", "이름"]도 후보키가 될 수 있을 때 먼저 가장 적은 갯수의 조합으로 후보키를 구한다


#주의2 (여기서 너무 헷갈렸다)
1. 예를 들어, ["학번"]을 후보키로 구했다고 했을 때, 그 후에는 ["학번"]이 다른 후보키에 들어가면 안되기 때문에 ["학번", "..."], ["학번", "...", "..."]은 후보키가 될 수 없다
2. 다른 예시로, ["학번, "이름"]을 후보키로 구했다고 했을 때, 그 후에는 ["학번", "이름", "..."], ["학번", "이름", "...", "..."]은 후보키가 될 수 없다 
3. 하지만, ["학번", "이름"]을 후보키로 구했다고 했을 때, 그 후에는 ["학번", "..."], ["이름", "..."]은 후보키가 될 수 있다
4. 따라서 마지막 예시로,
    0      1      2     3    4
[["100", "abc", "efg", "c", "z"],
["200", "abc", "hij", "c", "y"],
["300", "abc", "efg", "d", "z"],
["400", "abcd", "hij", "d", "z"]]
처럼 있을 때 후보키가 될 수 있는 조합은 [0], [2,3], [1,3,4] 로 답이 3이 된다


#풀이
1. 최소성을 만족해야하기 때문에 조합의 개수 1개부터 시작한다
    - 조합의 갯수 1개일 때(인덱스 이용) 모든 조합은 [0] ,[1] ,[2] ,[3] 이다
2. 각 조합의 값이 중복값이 있는지 유일성 검사를 한다
   - 딕셔너리와 최종 길이를 이용했지만, 방법은 매우 많을 것 같다
   - (여러개의 인덱스 조합일 때는 단순히 문자열로 이어붙여서 진행했다)
3. 최소성 검사를 진행한다 
- 위의 주의에서 말했듯이, 이미 구한 후보키가 속해있는지 검사한다
- 후보키를 구했다면, 후보키 조합을 저장해둔다
4. 과정1로 돌아가서 조합의 개수 1개부터 늘려가면서 최대 조합의 갯수( len(relations[0]) )까지 반복하여 구한다
'''