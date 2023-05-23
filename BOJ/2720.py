L = [25, 10, 5, 1]

for _ in range(int(input())):
  cents = int(input())
  money = [0, 0, 0, 0]

  for i in range(len(L)):
    money[i] = cents // L[i]
    cents -= money[i] * L[i]

  print(" ".join(map(str, money)))
