matrix = [list(map(int, input().split())) for _ in range(9)]

maxval = -1
row, col = -1, -1

for y in range(len(matrix)):
  for x in range(len(matrix[y])):
    if matrix[y][x] > maxval:
      maxval = matrix[y][x]
      row, col = y + 1, x + 1

print(maxval)
print(row, col)