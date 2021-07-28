# Second written code
#   - Accepted

import sys
input = sys.stdin.readline

# BOARD: 초록색 보드, 파란색 보드. 각각 4X6 크기에 빈칸은 -1로 초기화
# "보드 구분" = 초록색 보드는 0, 파란색 보드는 1 (== BOARD의 인덱스)
BOARD = [[[-1 for _ in range(4)] for _ in range(6)], [[-1 for _ in range(4)] for _ in range(6)]]
# BLOCKINFO: 각 보드마다 설치된 블럭의 정보 저장
# 블럭 정보는 튜플로 구성 = (인덱스, X 위치, Y 위치)
BLOCKINFO = [{}, {}]
# SCORE: 행/열이 블럭으로 채워져 지워진 횟수
SCORE = 0


### 하위 함수 ###
# calculateFallYLevel(보드 구분, 블럭 인덱스)
#    블럭이 떨어질 경우 멈추게 되는 Y 위치값을 리턴
def calculateFallYLevel(direction, blockIndex):
    shape, x, y = BLOCKINFO[direction][blockIndex]
    fallYLevel = y # 현재 Y 위치값에서 탐색 시작

    # Top-down 탐색, 블럭 모양이 3인 경우 탐색 종료 Y값 바운더리를 1 줄임
    # 내려가면서 탐색하다가 빈 공간 혹은 자신의 블럭이 아닌 다른 블럭이 존재할 경우 탐색 종료
    for nextY in range(y, 6 if shape != 3 else 5):
        # (x, y)
        blockIndex_X_Y = BOARD[direction][nextY][x]
        # 탐색할 위치의 블럭의 인덱스 값이 현재 블럭과 일치하면 칸이 비어있는 것으로 가정
        if blockIndex_X_Y == blockIndex:
            blockIndex_X_Y = -1

        if blockIndex_X_Y == -1:
            if shape == 1:
                fallYLevel = nextY
            elif shape == 2:
                # (x + 1, y)
                blockIndex_X1_Y = BOARD[direction][nextY][x + 1]
                if blockIndex_X1_Y == blockIndex:
                    blockIndex_X1_Y = -1
                
                if blockIndex_X1_Y == -1:
                    fallYLevel = nextY
                else:
                    break
            elif shape == 3:
                # (x, y + 1)
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

# checkAndUpdateSlicedT3(보드 구분, 블럭 인덱스, 확인할 블럭의 현재 X 위치값, 확인할 블럭의 현재 Y 위치값)
#    블럭 모양이 3이였던 블럭이 잘리게 된 경우, 모양을 확인하고 BLOCKINFO에 해당 블럭 정보 업데이트
def checkAndUpdateSlicedT3(direction, blockIndex, x, y):
    # (x, y - 1)의 블럭 인덱스
    aboveBlockIndex = BOARD[direction][y - 1][x] if y > 0 else -1
    # (x, y + 1)의 블럭 인덱스
    belowBlockIndex = BOARD[direction][y + 1][x] if y < 5 else -1

    # 상하 블럭이 모두 현재 블럭의 인덱스를 갖고있지 않은 경우
    if aboveBlockIndex != blockIndex and belowBlockIndex != blockIndex:
        # BLOCKINFO에 현재 블럭의 모양을 1로 저장
        BLOCKINFO[direction][blockIndex] = (1, x, y)

# moveBlock(보드 구분, 블럭 인덱스, 이동 목표 X 위치값, 이동 목표 Y 위치값)
#    블럭을 목표 위치로 옮기고 BOARD 업데이트
def moveBlock(direction, blockIndex, toX, toY):
    shape, fromX, fromY = BLOCKINFO[direction][blockIndex]

    # 기존 블럭 위치를 빈 공간으로 비움
    BOARD[direction][fromY][fromX] = -1
    if   shape == 2: BOARD[direction][fromY][fromX + 1] = -1
    elif shape == 3: BOARD[direction][fromY + 1][fromX] = -1

    # 목표 위치로 블럭 옮기기
    BOARD[direction][toY][toX] = blockIndex
    if   shape == 2: BOARD[direction][toY][toX + 1] = blockIndex
    elif shape == 3: BOARD[direction][toY + 1][toX] = blockIndex

    # BLOCKINFO에 옮긴 블럭 정보 업데이트
    BLOCKINFO[direction][blockIndex] = (shape, toX, toY)

# fallAllBlocks(보드 구분)
#    보드에 있는 모든 블럭을 떨어뜨릴 수 있으면 떨어뜨리기
def fallAllBlocks(direction):
    # 모양이 1이 아닌 블럭을 중복 처리하지 않도록 처리된 블럭 목록을 따로 저장
    processedBlockIndexes = []

    # Bottom-up 탐색
    for y in range(5, -1, -1):
        for x in range(4):
            blockIndex = BOARD[direction][y][x]

            if blockIndex == -1: continue
            elif (blockIndex != -1) and (not blockIndex in processedBlockIndexes):
                shape, origX, _ = BLOCKINFO[direction][blockIndex]

                # 블럭 모양이 3인 경우, 이전 작업(행/열 지우기)에서 블럭이 잘려졌는지 체크 및 블럭 정보 업데이트
                if shape == 3:
                    checkAndUpdateSlicedT3(direction, blockIndex, x, y)
                    shape, origX, _ = BLOCKINFO[direction][blockIndex]
                
                fallYLevel = calculateFallYLevel(direction, blockIndex)

                moveBlock(direction, blockIndex, origX, fallYLevel)
                processedBlockIndexes.append(blockIndex)

# canClearLine(행 혹은 열 리스트)
#    행 혹은 열을 지울 수 있는지 여부를 불리언으로 반환
def canClearLine(line):
    if -1 in line:
        return False
    return True

# clearLine(보드 구분, zero-based 행 혹은 열 번호)
#    해당 행 혹은 열을 보드에서 지우고 SCORE에 1 더하기
def clearLine(direction, lineNum):
    global SCORE

    BOARD[direction][lineNum] = [-1 for _ in range(4)]
    SCORE += 1


### 메인 프로시저에서 사용되는 함수 ###
# placeBlock(보드 구분, 블럭 인덱스, 블럭 모양, 빨간색 보드 내 X 위치값, 빨간색 보드 내 Y 위치값)
#    블럭을 배치하고 해당 보드로 떨어뜨리는 작업까지 수행
def placeBlock(direction, blockIndex, shape, x, y):
    # 파란색 보드가 대상일 경우 블럭 모양 및 X/Y 위치값 뒤집기
    if direction == 1:
        if   shape == 2: shape = 3
        elif shape == 3: shape = 2
        x, y = y, x
    
    # 다음 함수 호출 전 BLOCKINFO에 블럭 정보를 먼저 등록
    # Y 위치값은 현재 보드 최상단에 있는 것으로 가정 (어차피 떨어뜨릴 것이므로)
    BLOCKINFO[direction][blockIndex] = (shape, x, 0)

    placeYLevel = calculateFallYLevel(direction, blockIndex)
    moveBlock(direction, blockIndex, x, placeYLevel)

# processBoard(보드 구분)
#    보드를 문제에서 제시한 대로 처리
def processBoard(direction):
    # 루프 시작
    while True:
        hasChange = False

        ## 행/열 지우기로 점수 획득
        lineClearTargets = []
        
        # 2개 이상의 행/열이 지울 수 있으면 한 번에 지워야함
        for y in range(2, 6):
            if canClearLine(BOARD[direction][y]):
                lineClearTargets.append(y)

        if lineClearTargets:
            # 지울 수 있는 행/열을 한 번에 지우기
            for line in lineClearTargets:
                clearLine(direction, line)
            
            # 보드 내 모든 블럭 떨어뜨리기
            fallAllBlocks(direction)

            # 변경 사항이 존재한다는 플래그 업데이트
            hasChange = True
            
            # 행/열 지우기 처리 후 또 지울 수 있는 행/열이 있는지 확인하기 위해 연한 칸 처리 건너뛰기
            continue
        
        ## 연한 칸 처리
        specialLineTargetNum = 0

        # 2개의 연한 행/열에 블럭이 있다면 한 번에 처리해야함
        for y in range(2):
            if list(set(BOARD[direction][y])) != [-1]:
                specialLineTargetNum += 1
        
        if specialLineTargetNum > 0:
            # 처리 가능한 연한 행/열이 있다면 처리
            for _ in range(specialLineTargetNum):
                # 보드의 끝 행/열 제거
                del BOARD[direction][-1]
                # 보드의 처음 부분에 빈 행/열 삽입
                BOARD[direction].insert(0, [-1 for _ in range(4)])

            # 블럭들의 정보 업데이트
            processedBlockIndexes = []
            for y in range(2, 6):
                for x in range(4):
                    blockIndex = BOARD[direction][y][x]

                    if (blockIndex != -1) and (not blockIndex in processedBlockIndexes):
                        shape, origX, _ = BLOCKINFO[direction][blockIndex]

                        # 블럭 정보의 Y 위치값 업데이트
                        BLOCKINFO[direction][blockIndex] = (shape, origX, y)
            
                        # 블럭 모양이 3인 경우 잘렸는지 확인 후 업데이트
                        if shape == 3:
                            checkAndUpdateSlicedT3(direction, blockIndex, x, y)
                        
                        # 이미 처리한 블럭의 중복처리 방지
                        processedBlockIndexes.append(blockIndex)

            # 변경 사항이 존재한다는 플래그 업데이트
            hasChange = True

        ## 보드에 변경 사항이 없다면 루프 종료
        if not hasChange:
            break


### 메인 프로시저 ###
if __name__ == "__main__":
    N = int(input().rstrip())

    # 입력
    for i in range(N):
        # t = 블럭 모양 (1, 2, 3), y = 빨간색 보드 내 Y 위치값, x = 빨간색 보드 내 X 위치값
        t, y, x = map(int, input().split())

        # 블럭 배치
        placeBlock(0, i, t, x, y)
        placeBlock(1, i, t, x, y)

        # 보드 처리
        processBoard(0)
        processBoard(1)

        # for i in range(2):
        #     for y in range(6):
        #         print(BOARD[i][y])
        #     print()
    
    # 두 보드에 남아있는 모든 블럭의 개수 계산
    count = 0
    for board in BOARD:
        for y in range(6):
            for x in range(4):
                if board[y][x] != -1:
                    count += 1
    
    # 출력
    print(SCORE)
    print(count)