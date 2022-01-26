import sys

input = sys.stdin.readline

N = int(input())
SCORES = sorted([int(input()) for _ in range(N)])

def roundNG(num):
  return int(num) + 1 if num - int(num) >= 0.5 else int(num)

if N != 0:
  cutThreshold = roundNG(N * 0.15)
  SCORES = SCORES[cutThreshold:len(SCORES) - cutThreshold]

  print(roundNG(sum(SCORES) / len(SCORES)))
else:
  print(0)
