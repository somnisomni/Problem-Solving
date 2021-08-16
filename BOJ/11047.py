N, K = map(int, input().split())
A = list(reversed([int(input()) for _ in range(N)]))
coin = 0

def solve():
    global K, A, coin

    # Greedy
    for a in A:
        if (K // a) >= 1:
            coin += K // a
            K -= a * (K // a)

solve()
print(coin)