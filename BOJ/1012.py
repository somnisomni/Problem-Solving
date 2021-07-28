# https://velog.io/@jengyoung/baekjoon1012
# 1. 출력해야 하는 값은 총 section의 개수. 따라서 cnt 변수 설정.
# 2. field : 입력 받은 배열, visited : 기존 탐색 여부를 체크하는 배열
# 3. dfs function : 계속 field의 위, 아래, 왼쪽, 오른쪽 탐색하며 1이 있지만 방문하지 않은 곳을 체크해줌.
# 4. 반복문을 통해 array 전체를 탐색, 계속해서 1이 있지만 방문하지 않은 곳만 dfs함수 실행. 이후 cnt를 조건에 맞게 체크.

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)

T = int(input().rstrip())

def dfs(x, y):
    # 주변 체크 좌표 델타 (경우 4개) : d(0, 1) 위 -> d(0, -1) 아래 -> d(1, 0) 오른쪽 -> d(-1, 0) 왼쪽
    deltaX = [0, 0, 1, -1]
    deltaY = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + deltaX[i], y + deltaY[i]

        if nx >= 0 and ny >= 0 and nx < M and ny < N:   # Boundary check
            if farm[ny][nx] and not visited[ny][nx]:    # Availability check
                visited[ny][nx] = True
                dfs(nx, ny)
        else:
            continue

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    areas = 0

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = True

    for i in range(N):
        for j in range(M):
            if farm[i][j] and not visited[i][j]:
                visited[i][j] = True
                areas += 1
                dfs(j, i)

    print(areas)
