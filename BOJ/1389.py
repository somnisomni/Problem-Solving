LINKS = dict()

processStack = []
def lengthWithin(current, search, num=0):
  global processStack

  num += 1

  if not search in LINKS[current]:
    forwardMin = 999999

    for x in LINKS[current]:
      if x in processStack: continue

      processStack.append(x)
      forwardMin = min(forwardMin, lengthWithin(x, search, num))
      processStack = processStack[:-1]

    num = forwardMin
  
  return num
  
if __name__ == "__main__":
  N, M = map(int, input().split())

  for i in range(M):
    a, b = map(int, input().split())
    if not a in LINKS: LINKS[a] = []
    if not b in LINKS: LINKS[b] = []

    LINKS[a].append(b)
    LINKS[b].append(a)
  ###

  minimumIndex = -1
  minimumVal = 999999

  for i in range(1, N + 1):
    kbn = 0

    for j in range(1, N + 1):
      if i == j: continue
      kbn += lengthWithin(i, j)
    
    if minimumVal > kbn:
      minimumIndex = i
      minimumVal = kbn
  
  print(minimumIndex)
