# 2667번 코드 응용
import sys
sys.setrecursionlimit(100 * 100)
input = sys.stdin.readline

N = int(input())
AREA = [input().rstrip() for _ in range(N)]
VISITED_NORMAL = [[False] * N for _ in range(N)]
VISITED_COLORBLIND = [[False] * N for _ in range(N)]
countNormal = 0
countColorBlind = 0

def dfs(x, y, colorBlind):
    global countNormal, countColorBlind

    startColor = AREA[y][x]

    def realDFS(x, y):
        deltaX = [0, 0, 1, -1]
        deltaY = [1, -1, 0, 0]

        for i in range(4):
            nx, ny = x + deltaX[i], y + deltaY[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < N:
                if colorBlind:
                    if not VISITED_COLORBLIND[ny][nx] and \
                        (AREA[ny][nx] == startColor or \
                         (startColor == 'R' and AREA[ny][nx] == 'G') or \
                         (startColor == 'G' and AREA[ny][nx] == 'R')):
                        VISITED_COLORBLIND[ny][nx] = True
                        realDFS(nx, ny)
                else:
                    if not VISITED_NORMAL[ny][nx] and AREA[ny][nx] == startColor:
                        VISITED_NORMAL[ny][nx] = True
                        realDFS(nx, ny)
            else:
                continue
    
    realDFS(x, y)

    if colorBlind: countColorBlind += 1
    else: countNormal += 1

if __name__ == "__main__":
    for y in range(N):
        for x in range(N):
            if not VISITED_NORMAL[y][x]:
                VISITED_NORMAL[y][x] = True
                dfs(x, y, False)
            if not VISITED_COLORBLIND[y][x]:
                VISITED_COLORBLIND[y][x] = True
                dfs(x, y, True)
    
    print(countNormal, countColorBlind)
