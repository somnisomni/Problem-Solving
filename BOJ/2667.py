# Similar problem : 1012

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

N = int(input().rstrip())
apt = [[False] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(x, y):
    count = 1

    def realDFS(x, y):
        nonlocal count

        deltaX = [0, 0, 1, -1]
        deltaY = [1, -1, 0, 0]

        for i in range(4):
            nx, ny = x + deltaX[i], y + deltaY[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if apt[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    count += 1
                    realDFS(nx, ny)
            else:
                continue
    
    realDFS(x, y)
    return count

# len(areas) => area count, areas[areaIndex] = area element count
areas = []

for i in range(N):
    line = input().rstrip()

    for j in range(len(line)):
        if line[j] == "1":
            apt[i][j] = True

for i in range(N):
    for j in range(N):
        if apt[i][j] and not visited[i][j]:
            visited[i][j] = True
            areas.append(dfs(j, i))

areas = sorted(areas)

print(len(areas))
for area in areas: print(area)