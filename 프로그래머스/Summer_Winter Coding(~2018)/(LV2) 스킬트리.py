#LV2 스킬트리

def solution(skill, skill_trees):
    skill_list = list(skill)  #스킬 순서 알려주는 리스트
    answer = 0

    for skill_tree in skill_trees:   
        count = 0
        for i in range(len(skill_tree)):  #문자 하나씩 검사
            if skill_tree[i] in skill:  #문자가 스킬 순서 알려주는 리스트에 있는지 검사
                if skill_tree[i] == skill_list[count]: #문자가 skill_list[count]순서에 맞다면  
                    count += 1  #count +1 해주기!!

                else:  #순서가 맞지 않다면
                    answer += 1
                    break

    return len(skill_trees) - answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))


#Point
#문자 하나당 모두 검사하고, 스킬 순서에 있는 문자인지 확인하고, count사용하여 skill_list[count]처럼 사용하기!!



