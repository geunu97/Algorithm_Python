#LV2 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    bridge = deque(bridge)

    answer = 0
    count = 0
    for i in truck_weights:
        while True:
            answer += 1
            value = bridge.popleft()
            if value != 0:
                count -= 1
            
            if sum(bridge) + i <= weight and count < bridge_length:
                bridge.append(i)
                count += 1
                break
            else:
                bridge.append(0)
    
    
    return bridge_length + answer    #마지막 남아있는 거 처리


#Point (큐 문제)
#문제가 쪼금 이상?   
#1초에 한칸씩 이동한다는 말이 없음 -> 그래서 예제2에서 헷갈렸음