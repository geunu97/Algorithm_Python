# 아기 상어

'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

count = 0
x = 0
y = 0
start = []
graph = []
for i in range(N):
    list_a = list(map(int,input().split()))
    graph.append(list_a)

    for j in range(len(list_a)):
        if 1 <= list_a[j] <= 6:
            count += 1
        elif list_a[j] == 9:
            x = i
            y = j

shark_size = 2

dx = [1,0,-1,0]
dy = [0,-1,0,1]

while True:

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if graph[nx][ny] == shark_size:
                graph[nx][ny] = 0
                x = nx
                y = ny

            elif graph[nx][ny] < shark_size:
                shark_size += 1
                graph[nx][ny] = 0
                x = nx
                y = ny
'''