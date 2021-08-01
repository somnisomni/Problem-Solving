import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

def solve(x, y):
    if x >= N:
        return 0
    
    if dp[y][x] == -1:
        dp[y][x] = max(board[y][x] + solve(x + 1, y ^ 1), board[y][x] + solve(x + 2, y ^ 1))
    
    return dp[y][x]

for _ in range(T):
    N = int(input())
    board = [list(map(int, input().split())), list(map(int, input().split()))]
    dp = [[-1] * N, [-1] * N]

    solve(0, 0)
    solve(0, 1)

    print(max(dp[0][0], dp[1][0]))