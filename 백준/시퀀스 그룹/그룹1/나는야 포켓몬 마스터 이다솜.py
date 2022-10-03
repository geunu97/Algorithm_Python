import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dictionary = {}
for i in range(1,n+1):
  s = input().rstrip()
  dictionary[s] = i
  dictionary[str(i)] = s

for i in range(m):
  s = input().rstrip()
  print(dictionary[s])


#기본적인 해쉬(딕셔너리) 문제