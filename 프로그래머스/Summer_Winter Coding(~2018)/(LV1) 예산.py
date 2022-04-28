#LV1 예산

def solution(d, budget):
    d = sorted(d)
    
    sum = 0
    count = 0
    for i in range(len(d)):
        sum += d[i]
        if sum <= budget:
            count += 1
            continue
        else:
            break
            
    return count