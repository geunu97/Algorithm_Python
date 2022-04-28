#24단계: DFS와 BFS
#8. 수빈이는 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#   수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기

from collections import deque

N,K = map(int,input().split())

distance = [0] * 100001     #거리 나타내는 리스트 만들어주기!!!

dx = [-1,1]

q = deque([N])

while q:
    n = q.popleft()

    if n == K:
        break

    for i in range(3):     #총 3방향
        if i == 2:
            nx = n * 2
        else:
            nx = n + dx[i]

        if nx >= 0 and nx <= 100000:
            if distance[nx] == 0:   #아직 방문하지 않은 곳이라면!!!!
                distance[nx] = distance[n] + 1   #거리 +1씩 해주기
                q.append(nx)

print(distance[K])   #K번째 인덱스 (출발점까지 K번째까지 최단거리!!) 출력


#Point
#최단거리 살짝 변형문제 
#BFS