# PADOVAN SEQUENCE
# P(n) = P(n - 2) + P(n - 3)

mem = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 5, 9: 7, 10: 9}

def padovan(n):
    try:
        if not mem.get(n):
            mem[n] = padovan(n - 2) + padovan(n - 3)
    finally:
        return mem[n]

for _ in range(int(input())):
    print(padovan(int(input())))
