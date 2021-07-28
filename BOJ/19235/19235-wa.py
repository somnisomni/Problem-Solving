# First written code
#   - Wrong Answer

# T = 1   WIDTH 1 x HEIGHT 1
# T = 2   WIDTH 2 x HEIGHT 1   TURN TO T = 3 ON RIGHT BOARD IN THIS CODE
# T = 3   WIDTH 1 x HEIGHT 2   TURN TO T = 2 ON RIGHT BOARD IN THIS CODE

N = int(input())
boards = [[[-1 for _ in range(4)] for _ in range(6)], [[-1 for _ in range(4)] for _ in range(6)]]
# board#1 = Bottom board, board#2 = Right board
# Right board: flipped horizontally
boardsBlockInfo = [{}, {}]
# BlockInfo tuple = (shape, x, y)
score = 0

### Subfunctions ###
def findBlockFallYOffset(index, shape, direction, x, ylimit=0):
    fallYOffset = 5 - (1 if shape == 3 else 0)

    for b in range(fallYOffset, ylimit - 1, -1):
        newPosIndex = boards[direction][b][x]
        if newPosIndex == index: newPosIndex = -1

        if shape == 1 and newPosIndex != -1:
            fallYOffset = b - 1
            continue
        
        if shape == 2:
            newPosX1Index = boards[direction][b][x + 1]
            if newPosX1Index == index: newPosX1Index = -1

            if newPosIndex != -1 or newPosX1Index != -1:
                fallYOffset = b - 1
                continue
        
        if shape == 3:
            newPosY1Index = boards[direction][b + 1][x]
            if newPosY1Index == index: newPosY1Index = -1

            if newPosIndex != -1 or newPosY1Index != -1:
                fallYOffset = b - 1
                continue

    return fallYOffset

def moveBlock(index, shape, direction, fromX, fromY, toX, toY):
    # cleanup original position
    if not (fromX == None and fromY == None):
        boards[direction][fromY][fromX] = -1
        if shape == 2: boards[direction][fromY][fromX + 1] = -1
        elif shape == 3:
            if fromY < 5:
                boards[direction][fromY + 1][fromX] = -1
            else:
                boards[direction][fromY - 1][fromX] = -1
    
    # real move
    if shape == 2:   boards[direction][toY][toX + 1] = index
    elif shape == 3: boards[direction][toY + 1][toX] = index
    boards[direction][toY][toX] = index

    # save block info to boardsBlockInfo
    boardsBlockInfo[direction][index] = (shape, toX, toY)

def checkT3Sliced(index, direction, x, y):
    # T = 3 can be sliced to T = 1 when clear/remove a line
    if (y == 5 and boards[direction][y - 1][x] != index) or \
       (y == 0 and boards[direction][y + 1][x] != index) or \
       ((y < 5 and y > 0) and ((boards[direction][y + 1][x] != index) and (boards[direction][y - 1][x] != index))):
        boardsBlockInfo[direction][index] = (1, x, y)


def fallBlocksOnBoard(direction):
    # Bottom-up seeking for blocks to be fallen
    processedBlocks = []

    for y in range(5, -1, -1):
        for x in range(4):
            index = boards[direction][y][x]

            if index == -1: continue
            elif index != -1 and not index in processedBlocks:
                shape, xx, yy = boardsBlockInfo[direction][index]

                if shape == 3:
                    checkT3Sliced(index, direction, xx, yy)
                    shape, xx, yy = boardsBlockInfo[direction][index]

                placeYOffset = findBlockFallYOffset(index, shape, direction, xx, yy)

                moveBlock(index, shape, direction, xx, yy, xx, placeYOffset)

                processedBlocks.append(index)

def canClear(lineList):
    if -1 in lineList:
        return False
    return True

def clear(direction, lineNum):
    global score

    boards[direction][lineNum] = [-1 for _ in range(4)]
    score += 1

### Functions to be used on MAIN procedure ###
def placeBlockAndFall(index, shape, direction, x, y):
    if direction == 1:
        if shape == 2: shape = 3
        elif shape == 3: shape = 2
        x, y = y, x
    
    placeYOffset = findBlockFallYOffset(index, shape, direction, x)
    moveBlock(index, shape, direction, None, None, x, placeYOffset)

def checkBoard(direction):
    while True:
        isThereChanges = False
        lineClearTargets = []
        specialLineTargets = []

        # 점수 획득(행/열 제거)
        for y in range(5, -1, -1):
            if canClear(boards[direction][y]):
                lineClearTargets.append(y)
        
        if lineClearTargets:
            for line in lineClearTargets:
                clear(direction, line)

            fallBlocksOnBoard(direction)
            isThereChanges = True

        # 연한 칸 처리
        for y in range(1, -1, -1):
            if list(set(boards[direction][y])) != [-1]:
                specialLineTargets.append(y)
        
        if specialLineTargets:
            for _ in range(len(specialLineTargets)):
                del boards[direction][-1]
                boards[direction].insert(0, [-1 for _ in range(4)])

            for x in range(4): # T=3 slice check only for last y level
                if boards[direction][5][x] != -1:
                    checkT3Sliced(boards[direction][5][x], direction, x, 5)

            isThereChanges = True
        
        #print(isThereChanges, lineClearTargets, specialLineTargets)
        if not isThereChanges: break

### MAIN procedure ###
if __name__ == "__main__":
    for i in range(N):
        t, y, x = map(int, input().split())
        placeBlockAndFall(i, t, 0, x, y)
        placeBlockAndFall(i, t, 1, x, y)

        checkBoard(0)
        checkBoard(1)

    cnt = 0
    for bIdx in range(2):
        for y in range(6):
            for x in range(4):
                if boards[bIdx][y][x] != -1:
                    cnt += 1

    print(score)
    print(cnt)