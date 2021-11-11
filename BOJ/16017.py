n = [int(input()) for _ in range(4)]

if n[0] >= 8 and n[3] >= 8 and n[1] == n[2]:
  print("ignore")
else:
  print("answer")
