# Sweeping Algorithm 참고: https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220907708368

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
L = {}

lowdate = 999999
highdate = 0

for _ in range(N):
  datefrom, dateto = map(lambda x: int("".join(x.split("-"))), input().split())

  if not datefrom in L:
    # L[start date] = (seq last end date, occurrences)
    L[datefrom] = [dateto, list()]
  else:
    if dateto > L[datefrom][0]:
      L[datefrom][1].append(L[datefrom][0])
      L[datefrom][0] = dateto
    else:
      L[datefrom][1].append(dateto)

  if datefrom < lowdate: lowdate = datefrom
  if dateto > highdate: highdate = dateto

# === #

datetolst = {}

lowdate_y = int(str(lowdate)[:4])
lowdate_m = int(str(lowdate)[4:])
highdate_y = int(str(highdate)[:4])
highdate_m = int(str(highdate)[4:])

maxoccur = 0
maxoccurdate = 0

for daty in range(lowdate_y, highdate_y + 1):
  for datm in range(1, 13):
    if (lowdate_y == daty and datm < lowdate_m) \
      or (highdate_y == daty and datm > highdate_m):
      continue

    dat = int(str(daty) + str(datm).zfill(2))

    if dat in L:
      datetolst[L[dat][0]] = 1
      for dat2 in L[dat][1]:
        datetolst[dat2] = 1

    if maxoccur < len(datetolst):
      maxoccur = len(datetolst)
      maxoccurdate = str(dat)[:4] + "-" + str(dat)[4:]

    if dat in datetolst:
      del datetolst[dat]

print(maxoccurdate)
