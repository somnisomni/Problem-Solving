import sys
input = sys.stdin.readline

N = int(input())
TIMETABLE = list(sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0])))
# ↑ 끝나는 시간 기준 정렬 (Primary 조건: 끝나는 시간, Secondary 조건: 시작 시간)
count = 0

# Greedy
lastEndTime = -1
for time in TIMETABLE:
    if time[0] >= lastEndTime:
        lastEndTime = time[1]
        count += 1

print(count)