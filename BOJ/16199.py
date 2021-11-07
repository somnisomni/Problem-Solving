birthY, birthM, birthD = map(int, input().split())
curY, curM, curD = map(int, input().split())

# 만 나이
if (curM > birthM) or (curM == birthM and curD >= birthD):
  print(curY - birthY - 0)
else:
  print(curY - birthY - 1)

print(curY - birthY + 1) # 세는 나이
print(curY - birthY) # 연 나이
