# 반례 (최소 -> 최대 vs 실제 최소 이동)
# 최소 -> 최대 로직
# 4 1 2 1
# 6 0 2 0
# 5 2 1 0
# 7 1 0 0
# 6 0 2 0
# 5 2 1 0
# 7 1 0 0
# ...
# 
# 4 1 2 1
# 6 0 1 1
# 8 0 0 0

K = int(input())
EGGS = list(map(int, input().split()))

def process(basketA, basketB):
    eggSum = sum(EGGS)
    print(*EGGS)