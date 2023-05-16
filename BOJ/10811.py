N, M = map(int, input().split())
arr = [n for n in range(1, N + 1)]

for _ in range(M):
  i, j = map(int, input().split())
  subarr = list(reversed(arr[i - 1:j]))
  arr = arr[:i - 1] + subarr + arr[j:]

print(" ".join(map(str, arr)))