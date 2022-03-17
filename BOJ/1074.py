N, r, c = map(int, input().split())
nth = 0

def dac(xleft, ytop, size):
  global r, c, nth

  if size <= 1 and ytop == r and xleft == c:
      return
  else:
    if c < xleft + size // 2 and r < ytop + size // 2:
      dac(xleft, ytop, size // 2) # LT
      return
      # Ignore afterwards check
    elif c >= xleft + size // 2 and r < ytop + size // 2:
      nth += (size // 2) ** 2 # LT
      dac(xleft + size // 2, ytop, size // 2) # RT
      return
      # Ignore afterwards check
    elif c < xleft + size // 2 and r >= ytop + size // 2:
      nth += 2 * ((size // 2) ** 2) # LT, RT
      dac(xleft, ytop + size // 2, size // 2) # LB
      return
      # Ignore afterwards check
    else:
      nth += 3 * ((size // 2) ** 2) # LT, RT, LB
      dac(xleft + size // 2, ytop + size // 2, size // 2) # RB
      return
      # Ignore afterwards check

if __name__ == "__main__":
  dac(0, 0, 2 ** N)
  print(nth)
