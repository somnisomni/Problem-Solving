import sys
input = sys.stdin.readline

# Quadtree

N = int(input().rstrip())
PAPER = [list(map(int, input().split())) for _ in range(N)]

blueCount = 0
whiteCount = 0

def quadtree(offsetX, offsetY, splitLen):
    global blueCount, whiteCount

    # 분할 공간의 (offsetX, offsetY)에 있는 색상
    currentColor = PAPER[offsetY][offsetX]

    # 분할 공간 체크
    for x in range(offsetX, offsetX + splitLen):
        for y in range(offsetY, offsetY + splitLen):
            # 체크 중 일치하지 않는 색상이 발견된 경우
            if currentColor != PAPER[y][x]:
                # 쿼드트리 4분할
                quadtree(offsetX, offsetY, splitLen // 2)                                   # 상단 좌측 (2사분면)
                quadtree(offsetX + splitLen // 2, offsetY, splitLen // 2)                   # 상단 우측 (1사분면)
                quadtree(offsetX, offsetY + splitLen // 2, splitLen // 2)                   # 하단 좌측 (3사분면)
                quadtree(offsetX + splitLen // 2, offsetY + splitLen // 2, splitLen // 2)   # 하단 우측 (4사분면)
                return
    
    # 분할 공간 체크 완료 - 모든 공간이 같은 색인 경우
    # 완전한 분할 공간의 색상 분류
    if currentColor == 0:   # 흰색
        whiteCount += 1
    elif currentColor == 1: # 파란색
        blueCount += 1

    return
    
# 색종이 최상단 최좌측에서 쿼드트리 분할 시작 (전체 변 길이부터 시작)
quadtree(0, 0, N)

# 출력
print(whiteCount)
print(blueCount)