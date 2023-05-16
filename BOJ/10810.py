N, M = map(int, input().split())
arr = [0 for _ in range(1, N + 1)]

for _ in range(M):
  i, j, k = map(int, input().split())
  for x in range(i - 1, j):
    arr[x] = k

print(" ".join(map(str, arr)))
