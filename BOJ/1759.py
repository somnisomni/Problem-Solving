passLen, charLen = map(int, input().split())
chars = list(sorted(input().split()))

passList = []
def process(index, currentSeq):
  global passList

  if len(currentSeq) < passLen:
    for i in range(index + 1, charLen):
      seq = currentSeq + chars[i]
      process(i, seq)
  else:
    vowelCount = 0

    for c in ["a", "e", "i", "o", "u"]:
      if c in currentSeq: vowelCount += 1
    
    if (vowelCount < 1) or ((passLen - vowelCount) < 2):
      return
    
    passList.append(currentSeq)

for i in range(charLen):
  process(i, chars[i])

print("\n".join(passList))
