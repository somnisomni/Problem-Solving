import sys

input = sys.stdin.readline

N, M = map(int, input().split())
passList = dict()

for _ in range(N):
    url, password = input().split()
    passList[url] = password

for _ in range(M):
    print(passList[input().rstrip()])