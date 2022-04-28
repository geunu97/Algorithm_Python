#LV3 기지국 설치
#N개의 아파트가 일렬로 있으며, stations에 있는 수는 이미 설치된 기지국이 있는 아파트 번호이며, w는 전파 도달범위이다
#아직 전파가 도달이 안된 아파트에 최소 개수로 기지국을 설치하여 모든 아파트에 전파가 도달하려고한다. 설치할 최소 기지국의 갯수 구하기 

import math

def solution(n, stations, w):
    result = 0
    distance = []

    #설치된 기지국 사이에 전파가 닿지 않는 거리를 저장
    for i in range(1, len(stations)):
        distance.append((stations[i]-w-1) - (stations[i-1]+w))

    #맨 앞 기지국 - 첫 번째 아파트 사이에 전파가 닿지 않는 거리
    distance.append(stations[0]-w-1)
    #맨 뒤 기지국 - 마지막 아파트 사이에 전파가 닿지 않는 거리
    distance.append(n - (stations[-1]+w))

    for i in distance:
        if i <= 0 :  #닿지 않는 거리가 0 이하일 때
            continue
        
        result += math.ceil(i / ((w*2) +1)) #닿지 않는 거리에 설치할 수 있는 최소개수를 더해주기

    return result

print(solution(11,[4,11],1))

#Point
#닿지 않는 거리만을 이용

