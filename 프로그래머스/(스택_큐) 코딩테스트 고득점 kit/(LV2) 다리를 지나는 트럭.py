#LV2 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    q_bridge = deque([0] * bridge_length)
    time_value = 0
    sum_value = 0
    
    for truck in truck_weights:
        while True:
            sum_value -= q_bridge.popleft()     #다리에서 무조건 1초에 한칸씩 이동 
            time_value += 1
            
            if sum_value + truck > weight:
                q_bridge.append(0)
            else:
                q_bridge.append(truck)
                sum_value += truck
                break
            
    return len(q_bridge) + time_value   #마지막 남아있는 거 처리
            

#큐 문제

#문제 잘 이해해야 됨 (다리의 길이가 정해져 있고, 다리에서 1초에 한칸씩 이동하는 것 [0,0])   