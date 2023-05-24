# TLE, possibly many loop?

import sys
input = sys.stdin.readline

N = int(input())
L = {}

for _ in range(N):
  datefrom, dateto = map(lambda x: tuple(map(int, x.split("-"))), input().split())

  for dat_y in range(datefrom[0], dateto[0] + 1):
    for dat_m in range(1, 12 + 1):
      datstr = str(dat_y) + str(dat_m).zfill(2)

      if dat_y == datefrom[0] and dat_m < datefrom[1]:
        continue
      else:
        if not datstr in L: L[datstr] = 0
        L[datstr] += 1

maxval, maxidx = -1, ""
for x in L.items():
  if x[1] > maxval:
    maxidx = x[0]
    maxval = x[1]

print(maxidx[:4] + "-" + maxidx[4:])
