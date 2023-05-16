board = [[0 for _ in range(100)] for _ in range(100)]

count = 0
for _ in range(int(input())):
  xoffset, yoffset = map(lambda x: x - 1, map(int, input().split()))

  for y in range(10):
    for x in range(10):
      if board[y + yoffset][x + xoffset] == 0:
        board[y + yoffset][x + xoffset] = 1
        count += 1

print(count)