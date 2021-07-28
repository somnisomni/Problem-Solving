import sys
input = sys.stdin.readline

N = int(input().rstrip())
DATA = [list(map(int, input().rstrip())) for _ in range(N)]

def quadtree(offsetX, offsetY, splitLen):
    flag = DATA[offsetY][offsetX]

    for x in range(offsetX, offsetX + splitLen):
        for y in range(offsetY, offsetY + splitLen):
            if flag != DATA[y][x]:
                lt = quadtree(offsetX, offsetY, splitLen // 2)
                rt = quadtree(offsetX + splitLen // 2, offsetY, splitLen // 2)
                lb = quadtree(offsetX, offsetY + splitLen // 2, splitLen // 2)
                rb = quadtree(offsetX + splitLen // 2, offsetY + splitLen // 2, splitLen // 2)
                return "(" + str(lt) + str(rt) + str(lb) + str(rb) + ")"
    
    return flag

print(quadtree(0, 0, N))