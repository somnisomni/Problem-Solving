import sys
input = sys.stdin.readline

Lf = {}
Lt = {}
dl = 999999
dh = 0

for _ in range(int(input())):
  dfrom, dto = map(lambda x: int("".join(x.split("-"))), input().split())

  if not dfrom in Lf: Lf[dfrom] = 1
  else: Lf[dfrom] += 1
  if not dto in Lt: Lt[dto] = 1
  else: Lt[dto] += 1

  if dfrom < dl: dl = dfrom
  if dto > dh: dh = dto

o = 0
mo = 0
mod = ""

for d in range(dl, dh + 1):
  if d in Lf:
    o += Lf[d]
    del Lf[d]

  if mo < o:
    mo = o
    mod = d

  if d in Lt:
    o -= Lt[d]
    del Lt[d]

print(str(mod)[:4] + "-" + str(mod)[4:])
