# 참고 : https://infinitt.tistory.com/229
# 문제에서 원하는 출력은 (버블정렬이 일어난 횟수 + 1)

# 버블정렬은 1회 정렬에 한 요소가 리스트의 뒤로는 무한정 갈 수 있어도 앞으로는 최대 1회만 갈 수 있다.
# 이를 이용해, 정렬 전 리스트와 정렬 후 리스트를 비교하여 앞으로 간 요소(인덱스 차이 값이 양수)의
# 인덱스 차이가 가장 큰 값이 곧 버블정렬이 일어난 횟수이다.

import sys
input = sys.stdin.readline

N = int(input())
A = [(int(input()), index) for index in range(N)]

# 버블정렬을 굳이 구현할 필요가 없다. 어찌됐든 정렬된 리스트만 필요
sortedA = list(sorted(A))

# 인덱스 차이 최대값 비교
maxDiff = 0
for i in range(len(A)):
    maxDiff = max(sortedA[i][1] - A[i][1], maxDiff)

# 출력
print(maxDiff + 1)