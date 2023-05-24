import sys
input = sys.stdin.readline

Lfrom = {}
Lto = {}
low = 999999
high = 0

for _ in range(int(input())):
  datefrom, dateto = map(lambda x: int("".join(x.split("-"))), input().split())

  if not datefrom in Lfrom: Lfrom[datefrom] = 1
  else: Lfrom[datefrom] += 1
  if not dateto in Lto: Lto[dateto] = 1
  else: Lto[dateto] += 1

  if datefrom < low: low = datefrom
  if dateto > high: high = dateto

low_y, low_m = int(str(low)[:4]), int(str(low)[4:])
high_y, high_m = int(str(high)[:4]), int(str(high)[4:])
occ = 0
maxocc = 0
maxoccdate = ""

for dat in range(low, high + 1):
  dat_y, dat_m = int(str(dat)[:4]), int(str(dat)[4:])
  if (low_y == dat_y and dat_m < low_m) \
    or (high_y == dat_y and dat_m > high_m):
    continue

  if dat in Lfrom:
    occ += Lfrom[dat]
    del Lfrom[dat]

  if maxocc < occ:
    maxocc = occ
    maxoccdate = str(dat)[:4] + "-" + str(dat)[4:]

  if dat in Lto:
    occ -= Lto[dat]
    del Lto[dat]

print(maxoccdate)
