# N-Queen (Backtracking (DFS)) 문제
# 시뮬레이션처럼 접근한 코드
#
# 빈번한 deepcopy 발생으로 인해 TLE 발생

from copy import deepcopy

N = int(input())
BOARD_STACK = {0: [[-1 for _ in range(N)] for _ in range(N)]}
POSSIBLES = 0

def solve(y):
  global BOARD_STACK, POSSIBLES

  realY = y - 1

  if realY > N - 1: return

  BOARD_STACK[y] = deepcopy(BOARD_STACK[y - 1])

  placed = False
  for x in range(N):  # X axis iteration
    if BOARD_STACK[y - 1][realY][x] == -1:
      BOARD_STACK[y][realY] = [realY for _ in range(N)]  # X axis fill
      xoffset = 0
      for yt in range(realY, N):
        BOARD_STACK[y][yt][x] = realY  # upcoming Y axis fill
        if x + xoffset < N: BOARD_STACK[y][yt][x + xoffset] = realY  # upcoming right diag fill
        if x - xoffset >= 0: BOARD_STACK[y][yt][x - xoffset] = realY  # upcoming left diag fill
        xoffset += 1

      placed = True
      solve(y + 1)
      BOARD_STACK[y] = deepcopy(BOARD_STACK[y - 1])
  
  if placed and realY == N - 1:
    POSSIBLES += 1

if __name__ == "__main__":
  solve(1)
  print(POSSIBLES)
