import sys
sys.setrecursionlimit(10000)    #재귀 깊이 설정해줘야 함

dictionary = {}
result = []

def re(number,visited):
    if number not in dictionary:
        dictionary[number] = number + 1
        result.append(number)
        for i in visited:
            dictionary[i] = number + 1
        return 

    else:
        visited.append(number)
        re(dictionary[number],visited)

        
        
def solution(k, room_number):
    for number in room_number:
        re(number,[])
    
    return result



#딕셔너리 활용 {원하는 방번호: 다음 빈방 번호}
#재귀 활용 (다음 빈방 번호를 활용해서 재귀로 딕셔너리에 없는 값(빈 방) 찾기)


#1. 순서대로 room_number배열 진행

#2-1. 원하는 방 번호가 딕셔너리에 없다면(= 빈 방이라면)
#   딕셔너리에 {원하는 방 번호: 원하는 방 번호+1} 넣기
#   {방문했던 원하는 방들 모두: 빈 방+1}  
#   return

#2-2. 원하는 방 번호가 딕셔너리에 있다면(= 빈 방이 아니라면)
#   딕셔너리의 {원하는 방 번호가 가리키는 value값}을 재귀값으로 넣기 
#   방문했던 원하는 방 번호 모으기 (visited)

