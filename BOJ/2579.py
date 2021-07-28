import sys
input = sys.stdin.readline

N = int(input().rstrip())
stairs = [-1]
dp = [-1] * (N + 1)

def stairDP(level):
    if dp[level] == -1:
        dp[level] = max( \
            stairDP(level - 3) + stairs[level - 1], \
            stairDP(level - 2)) + stairs[level]

    return dp[level]

for _ in range(N):
    stairs.append(int(input().rstrip()))

dp[0] = 0
dp[1] = stairs[1]

if N >= 2: dp[2] = stairs[1] + stairs[2]

print(stairDP(N))