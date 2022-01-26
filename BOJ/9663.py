N = int(input())
ROWS = [-999] * N
POSSIBLES = 0

def isPlaceable(y, x):
  # Find for queens which is in same X position
  if x in ROWS: return False

  # Find for queens which is in diagonal
  xoffset = 1
  for yy in range(y - 1, -1, -1):
    if ROWS[yy] == x + xoffset or ROWS[yy] == x - xoffset:
      return False
    xoffset += 1
  
  return True

def solve(y):
  global ROWS, POSSIBLES

  if y > N - 1: return

  placed = False
  for x in range(N):
    if isPlaceable(y, x):
      ROWS[y] = x

      placed = True
      solve(y + 1)
  
  if placed and y == N - 1:
    POSSIBLES += 1
  
  ROWS[y] = -999

if __name__ == "__main__":
  solve(0)
  print(POSSIBLES)
