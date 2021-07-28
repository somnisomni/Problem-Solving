import sys
input = sys.stdin.readline

N = int(input().split()[2]) # #define quadtree_width N
DATA = []
input() # #define quadtree_height N
input() # static char quadtree_bits[] = {

def hexConvert(hexStr):
    # 이건 틀림 (헥사값 한번에 변환)
    # # 각 헥사 값은 8비트 => "{0:08b}".format(...)   # format의 숫자형 매개변수는 2진수로 변환되어 포맷됨
    # # 픽셀이 오른쪽에서 왼쪽으로 변환되어 구성 => int(hexStr[2:][::-1], 16)   # 선행 '0x' 텍스트를 지우고 순수 헥사 값 뒤집은 후 16진수(헥사)로 변환
    # # B = 0b1, W = 0b0 => .replace("1", "B").replace("0", "W")
    # return "{0:08b}".format(int(hexStr[2:][::-1], 16)).replace("1", "B").replace("0", "W")

    # 요것도 틀림 (개별로 헥사값 변환하긴 했는데 어쨌든 윗 방법이랑 똑같음)
    # sequence = ""
    # for hexSingleNum in hexStr[2:][::-1]:
    #     sequence += "{0:04b}".format(int(hexSingleNum, 16)).replace("1", "B").replace("0", "W")
    # return sequence

    # 2진수 변환 후 2진수값 자체를 뒤집고 처리
    return ("{0:08b}".format(int(hexStr[2:], 16)))[::-1].replace("1", "B").replace("0", "W")

for _ in range(N):
    dataTemp = list(map(hexConvert, input().split(",")[:-1]))
    DATA.append("".join(dataTemp))

input() # };

def quadtree(offsetX, offsetY, splitLen):
    flag = DATA[offsetY][offsetX]

    for x in range(offsetX, offsetX + splitLen):
        for y in range(offsetY, offsetY + splitLen):
            if flag != DATA[y][x]:
                lt = quadtree(offsetX, offsetY, splitLen // 2)
                rt = quadtree(offsetX + splitLen // 2, offsetY, splitLen // 2)
                lb = quadtree(offsetX, offsetY + splitLen // 2, splitLen // 2)
                rb = quadtree(offsetX + splitLen // 2, offsetY + splitLen // 2, splitLen // 2)
                return "Q" + str(lt) + str(rt) + str(lb) + str(rb)
    
    return flag

print(N)
print(quadtree(0, 0, N))