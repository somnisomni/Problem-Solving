# 19235번의 열화 버전 문제
# 19235번 AC 맞은 코드 재활용

import sys
input = sys.stdin.readline

BOARD = [[[-1 for _ in range(4)] for _ in range(6)], [[-1 for _ in range(4)] for _ in range(6)]]
BLOCKINFO = [{}, {}]
SCORE = 0

def calculateFallYLevel(direction, blockIndex):
    shape, x, y = BLOCKINFO[direction][blockIndex]
    fallYLevel = y
    for nextY in range(y, 6 if shape != 3 else 5):
        blockIndex_X_Y = BOARD[direction][nextY][x]
        if blockIndex_X_Y == blockIndex:
            blockIndex_X_Y = -1

        if blockIndex_X_Y == -1:
            if shape == 1:
                fallYLevel = nextY
            elif shape == 2:
                blockIndex_X1_Y = BOARD[direction][nextY][x + 1]
                if blockIndex_X1_Y == blockIndex:
                    blockIndex_X1_Y = -1
                
                if blockIndex_X1_Y == -1:
                    fallYLevel = nextY
                else:
                    break
            elif shape == 3:
                blockIndex_X_Y1 = BOARD[direction][nextY + 1][x]
                if blockIndex_X_Y1 == blockIndex:
                    blockIndex_X_Y1 = -1

                if blockIndex_X_Y1 == -1:
                    fallYLevel = nextY
                else:
                    break
        else:
            break
    
    return fallYLevel

def checkAndUpdateSlicedT3(direction, blockIndex, x, y):
    aboveBlockIndex = BOARD[direction][y - 1][x] if y > 0 else -1
    belowBlockIndex = BOARD[direction][y + 1][x] if y < 5 else -1

    if aboveBlockIndex != blockIndex and belowBlockIndex != blockIndex:
        BLOCKINFO[direction][blockIndex] = (1, x, y)

def moveBlock(direction, blockIndex, toX, toY):
    shape, fromX, fromY = BLOCKINFO[direction][blockIndex]

    BOARD[direction][fromY][fromX] = -1
    if   shape == 2: BOARD[direction][fromY][fromX + 1] = -1
    elif shape == 3: BOARD[direction][fromY + 1][fromX] = -1

    BOARD[direction][toY][toX] = blockIndex
    if   shape == 2: BOARD[direction][toY][toX + 1] = blockIndex
    elif shape == 3: BOARD[direction][toY + 1][toX] = blockIndex

    BLOCKINFO[direction][blockIndex] = (shape, toX, toY)

def canClearLine(line):
    if -1 in line:
        return False
    return True

def placeBlock(direction, blockIndex, shape, x, y):
    if direction == 1:
        if   shape == 2: shape = 3
        elif shape == 3: shape = 2
        x, y = y, x

    BLOCKINFO[direction][blockIndex] = (shape, x, 0)

    placeYLevel = calculateFallYLevel(direction, blockIndex)
    moveBlock(direction, blockIndex, x, placeYLevel)

def processBoard(direction):
    global SCORE

    while True:
        hasChange = False

        lineClearTargets = []
        for y in range(2, 6):
            if canClearLine(BOARD[direction][y]):
                lineClearTargets.append(y)

        if lineClearTargets:
            for line in lineClearTargets:
                del BOARD[direction][line]
                BOARD[direction].insert(0, [-1 for _ in range(4)])
                SCORE += 1

            hasChange = True

        specialLineTargetNum = 0
        for y in range(2):
            if list(set(BOARD[direction][y])) != [-1]:
                specialLineTargetNum += 1
        
        if specialLineTargetNum > 0:
            for _ in range(specialLineTargetNum):
                del BOARD[direction][-1]
                BOARD[direction].insert(0, [-1 for _ in range(4)])

            hasChange = True

        if hasChange:
            processedBlockIndexes = []
            for y in range(2, 6):
                for x in range(4):
                    blockIndex = BOARD[direction][y][x]

                    if (blockIndex != -1) and (not blockIndex in processedBlockIndexes):
                        shape, origX, _ = BLOCKINFO[direction][blockIndex]

                        BLOCKINFO[direction][blockIndex] = (shape, origX, y)

                        if shape == 3:
                            checkAndUpdateSlicedT3(direction, blockIndex, x, y)

                        processedBlockIndexes.append(blockIndex)
        else:
            break

if __name__ == "__main__":
    N = int(input().rstrip())

    for i in range(N):
        t, y, x = map(int, input().split())

        placeBlock(0, i, t, x, y)
        placeBlock(1, i, t, x, y)

        processBoard(0)
        processBoard(1)

    count = 0
    for board in BOARD:
        for y in range(6):
            for x in range(4):
                if board[y][x] != -1:
                    count += 1

    print(SCORE)
    print(count)