import sys
input = sys.stdin.readline

# Nonupletree? ww

N = int(input().rstrip())
PAPER = [list(map(int, input().split())) for _ in range(N)]

counts = [0] * 3

def nonupletree(offsetX, offsetY, splitLen):
    global counts

    currentNum = PAPER[offsetY][offsetX]

    for x in range(offsetX, offsetX + splitLen):
        for y in range(offsetY, offsetY + splitLen):
            if currentNum != PAPER[y][x]:
                sDiv3 = splitLen // 3
                sDiv3Mul2 = (splitLen // 3) * 2

                # Top Left
                nonupletree(offsetX, offsetY, sDiv3)
                # Top Center
                nonupletree(offsetX + sDiv3, offsetY, sDiv3)
                # Top Right
                nonupletree(offsetX + sDiv3Mul2, offsetY, sDiv3)
                # Middle Left
                nonupletree(offsetX, offsetY + sDiv3, sDiv3)
                # Middle Center
                nonupletree(offsetX + sDiv3, offsetY + sDiv3, sDiv3)
                # Middle Right
                nonupletree(offsetX + sDiv3Mul2, offsetY + sDiv3, sDiv3)
                # Bottom Left
                nonupletree(offsetX, offsetY + sDiv3Mul2, sDiv3)
                # Bottom Center
                nonupletree(offsetX + sDiv3, offsetY + sDiv3Mul2, sDiv3)
                # Bottom Right
                nonupletree(offsetX + sDiv3Mul2, offsetY + sDiv3Mul2, sDiv3)

                return

    counts[currentNum + 1] += 1

    return
    
nonupletree(0, 0, N)

print(counts[0])
print(counts[1])
print(counts[2])