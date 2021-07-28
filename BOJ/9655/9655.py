N = int(input())
sk = False

while True:
    if N == 0:
        break
    else:
        if N >= 3:
            N = N - 3
        else:
            N = N - 1
        
        sk = not sk

print("SK" if sk else "CY")