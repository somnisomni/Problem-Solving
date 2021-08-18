# Example C++ code to Python
# TLE on Python3 and PyPy3

import sys
input = sys.stdin.readline

N = int(input())
A = [None] + [int(input()) for _ in range(N)]

change = False
for i in range(1, N + 2):
    change = False

    for j in range(1, N - i + 1):
        if A[j] > A[j + 1]:
            change = True
            A[j], A[j + 1] = A[j + 1], A[j]
    
    if not change:
        print(i)
        break
