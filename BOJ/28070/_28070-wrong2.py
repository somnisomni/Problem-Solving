# Sweeping Algorithm 참고: https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220907708368

import sys
input = sys.stdin.readline

N = int(input())
L = {}

lowdate = 999999
highdate = 0

for _ in range(N):
  datefrom, dateto = map(lambda x: int("".join(x.split("-"))), input().split())

  if not datefrom in L:
    L[datefrom] = [dateto]
  else:
    L[datefrom].append(dateto)

  if datefrom < lowdate: lowdate = datefrom
  if dateto > highdate: highdate = dateto

# === #

L = dict(sorted(L.items(), key=lambda x: x[0]))
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
      for dat2 in L[dat]:
        datetolst[dat2] = 1

    # print(dat, len(datetolst), datetolst)

    if maxoccur < len(datetolst):
      maxoccur = len(datetolst)
      maxoccurdate = str(dat)[:4] + "-" + str(dat)[4:]

    if dat in datetolst:
      del datetolst[dat]

print(maxoccurdate)
