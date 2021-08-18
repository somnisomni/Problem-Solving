# Bubble Sort
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    lineCount = 0
    _, data = input(), list(map(int, input().split()))

    for i in range(len(data) - 1, -1, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                data[j + 1], data[j] = data[j], data[j + 1]
                lineCount += 1

    print(lineCount)