#LV1 소수 만들기

sosu_list = [-1] * 3000

for i in range(2,len(sosu_list)):
    if sosu_list[i] == -1:
        sosu_list[i] = True
    
    for j in range(i*2,len(sosu_list),i):
        if sosu_list[j] == -1:
            sosu_list[j] = False
    
def solution(nums):
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if sosu_list[nums[i]+nums[j]+nums[k]]:
                    count += 1      
                
    return count


print(solution([1,2,3,4]))


#Point
#반복문 3개로 3개 선택하기 (완전탐색) (아니면 itertools - combinations 사용해도됨)
#소수찾기 - 에라토스테네스의 체    





