import sys
input = sys.stdin.readline

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

def pooling(xleft, ytop, size):
  if size <= 2:
    seq = list(sorted([BOARD[xleft][ytop], BOARD[xleft + 1][ytop], BOARD[xleft][ytop + 1], BOARD[xleft + 1][ytop + 1]]))
    return seq[2]
  else:
    first = pooling(xleft, ytop, size // 2) # LT
    second = pooling(xleft + size // 2, ytop, size // 2) # RT
    third = pooling(xleft, ytop + size // 2, size // 2) # LB
    fourth = pooling(xleft + size // 2, ytop + size // 2, size // 2) # RB

    return list(sorted([first, second, third, fourth]))[2]

if __name__ == "__main__":
  print(pooling(0, 0, N))
