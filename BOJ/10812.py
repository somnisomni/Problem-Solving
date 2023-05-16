N, M = map(int, input().split())
arr = [n for n in range(1, N + 1)]

for _ in range(M):
  i, j, k = map(lambda x: x - 1, map(int, input().split()))

  beginArr = arr[i:k]
  endArr = arr[k:j + 1]
  arr = arr[:i] + endArr + beginArr + arr[j + 1:]

print(" ".join(map(str, arr)))