N, M = map(int, input().split())

matrix = [[0 for _ in range(M)] for _ in range(N)]

for y in range(N):
  matrix[y] = list(map(int, input().split()))

for y in range(N):
  line = list(map(int, input().split()))

  for x in range(M):
    matrix[y][x] += line[x]
  
  print(" ".join(map(str, matrix[y])))