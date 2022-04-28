#14단계: 백트래킹
#8. 스타트와 링크 (삼성 SW 역량 테스트 기출 문제 2)

'''
#방법1 파이썬으로 DFS구현 -> 시간초과
import sys
input = sys.stdin.readline

N = int(input())
min = 100000000

list_input=[]
for _ in range(N):
    list_a = list(map(int,input().split()))
    list_input.append(list_a)

list_new=[]
def DFS():
    if len(list_new) == N:
        team_div(list_new)
        return

    for i in range(N):
        if i not in list_new:
            list_new.append(i)
            DFS()
            list_new.pop()

def team_div(list_new):
    global min

    team1_sum_list=[]
    for i in range(len(list_new)//2):
        team1_sum_list.append(list_new[i])

    team2_sum_list=[]
    for j in range(len(list_new)//2,N):
        team2_sum_list.append(list_new[j])

    team1_sum_number = sum(team1_sum_list)
    team2_sum_number = sum(team2_sum_list)

    if min > abs(team1_sum_number - team2_sum_number):
        min = abs(team1_sum_number - team2_sum_number)

    return 

def sum(team_sum_list):
    sum = 0
    for i in team_sum_list:
        for j in team_sum_list:
            if i == j:
                continue
            else:
                sum += list_input[i][j]
    
    return sum

DFS()

print(min)
'''


#방법2 import itertools 사용

from itertools import combinations

N = int(input())

S = [list(map(int,input().split())) for _ in range(N)]
member = [i for i in range(N)]

team_combi = []
for team in combinations(member,N//2):
    team_combi.append(team)

min_result = 987654321
for k in range(len(team_combi)//2):

    team_a = team_combi[k]
    team_b = list(set(member) - set(team_combi[k]))

    start_team = 0
    for i in range(len(team_a)):
        for j in team_a:
            start_team += S[team_a[i]][j]

    link_team = 0
    for i in range(len(team_b)):
        for j in team_b:
            link_team += S[team_b[i]][j]

    min_result = min(min_result, abs(start_team - link_team))

print(min_result)
