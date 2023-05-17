import sys
input = sys.stdin.readline

input()

tower = list(map(int, input().split()))
cur = tower[0]
count = 1
for i in tower[1:]:
  if i >= cur:
    count += 1
  cur = i

print(count)
