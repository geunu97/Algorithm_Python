#LV3 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    answer = []
    tree = {"-":"root"}  #딕셔너리로 트리 만들기, 자식:부모
    sell = {"-":0} #딕셔너리로 각각 판매금액 나타내기
    
    for i in range(len(enroll)):  
        child = enroll[i]   #자식
        parent = referral[i] #부모
        tree[child] = parent  #차례대로 자식-부모 나타내는 딕셔너리 트리 만들기
        sell[child] = 0    #각각의 판매금액 나타내는 딕셔너리 만들기
        
    for i in range(len(seller)):
        child = seller[i]  #자식
        parent = tree[child] #부모
        money = amount[i] * 100  #자식의 판매금액
        sell[child] += money  #자식의 판매금액 딕셔너리에 더해주기

        while True:
            commission = money // 10   #수수료 
            if commission == 0:
                break
            sell[child] -= commission #자식한테 다시 수수료 빼주기
            sell[parent] += commission #부모한테 수수료 더해주기

            child = parent #자식 부모 변경, 한 단계 올라가기
            parent = tree[child] 
            money = commission
            
            if parent == "root": # 부모가 root이면 종료
                break

    answer = list(sell.values())[1:]  #sell딕셔너리 values 값만 뽑기 

    return answer


#Point
#자식:부모를 나타내는 트리를 딕셔너리로 만들기
#각각의 판매금액을 나타내는 딕셔너리 만들기

#반복적으로 seller에서부터 root까지 한단계씩 10%수수료씩 주기 (DFS)



