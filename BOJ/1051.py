N, M = map(int, input().split())
area = [input() for _ in range(N)]
maxSize = 1

for i in range(N - 1):
    for j in range(M - 1):
        edgeTL = area[i][j]

        for k in range(1, N - i):
            if j + k > M - 1: break

            edgeBL = area[i + k][j]
            edgeBR = area[i + k][j + k]
            edgeTR = area[i][j + k]

            if edgeTL == edgeBL == edgeBR == edgeTR:
                maxSize = max(maxSize, (k + 1) ** 2)

print(maxSize)