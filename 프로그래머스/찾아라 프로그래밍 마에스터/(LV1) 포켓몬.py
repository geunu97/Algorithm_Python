#LV1 포켓몬

# nums의 반절개 만큼 숫자를 선택할 때 최대한 많은 서로 다른 종류(숫자)를 선택해야 한다. 
# 최대 몇가지 종류가 나오는지 구하기  

def solution(nums):
    list_nums = list(set(nums))
    
    if len(list_nums) >= len(nums) // 2:
        return len(nums) // 2
    else:
        return len(list_nums)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))

#Point
#중복제거 사용   (list(set()))


