#LV3 베스트앨범

def solution(genres, plays):
    dictionary = {}
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in dictionary:
            dictionary[genre] = [plays[i],[plays[i],i]]        #딕셔너리에 없었다면, 리스트 형태로 넣기, [재생수, [재생수1,인덱스1]]
        else:
            dictionary[genre][0] += plays[i]                   #딕셔너리에 있다면, 재생수 합하고, 뒤에 노래 이어붙이기 [재생수 합하기, [재생수1,인덱스1]] 
            dictionary[genre].append([plays[i],i])             #[재생수 합하기, [재생수1,인덱스1], [재생수2,인덱스2]] 
    
    tuple = sorted(dictionary.items(), key=lambda x: (-x[1][0]))  #딕셔너리 value값기준으로 정렬하는법, value의 리스트첫번째 원소기준으로 정렬하기, 내림차순으로정렬
                                                                  #이런식을 정렬하면 튜플로 변환된다
    answer = []
    for i in tuple:
        i = i[1:]    #필요없는 부분 제거
        for j in i:
            j = j[1:]
            j = sorted(j, key=lambda x: (-x[0],x[1]))     #정렬
            
            answer.append(j[0][1])
            if len(j) >= 2:
                answer.append(j[1][1])
    
    return answer


#Point
#해쉬 문제 (딕셔너리)