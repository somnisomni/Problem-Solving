import sys
from collections import deque

Nbase10, B = map(int, sys.stdin.readline().split())
N = deque()

def find(exp):
  global Nbase10
  if Nbase10 % pow(B, exp) != Nbase10:
    return find(exp + 1)
  else:
    return exp

def conv_base(num):
  if 0 <= num <= 9: return str(num)
  else: return chr(ord("A") + num - 10)

if __name__ == "__main__":
  exp = find(1)
  num = 0

  # Iteration
  for e in range(exp - 1, -1, -1):
    num = Nbase10 // pow(B, e)
    N.append(conv_base(num))
    Nbase10 -= num * pow(B, e)

  sys.stdout.write("".join(N))
