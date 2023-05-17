inp = input().split()
N, B = inp[0], int(inp[1])
Nbase10 = []

for i in range(len(N)):
  x = N[i]
  if "0" <= x <= "9": Nbase10.append(int(x))
  elif "A" <= x <= "Z": Nbase10.append(10 + (ord(x) - ord("A")))

  Nbase10[i] *= pow(B, (len(N) - 1) - i)

print(sum(Nbase10))
