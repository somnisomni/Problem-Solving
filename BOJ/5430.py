from queue import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    func, n, array = input().rstrip(), int(input().rstrip()), deque(eval(input().rstrip()))
    cont = False
    lastR = False
    reverseStatus = False
    funcRCount = 0

    for i in range(len(func)):
        c = func[i]

        if c == "R":
            if not lastR: lastR = True
            else: lastR = False

            if i == len(func) - 1 and lastR:
                funcRCount += 1
        elif c == "D":
            if lastR:
                funcRCount += 1
                lastR = False
                reverseStatus = not reverseStatus
            
            if len(array) > 0:
                if reverseStatus:
                    array.pop()
                else:
                    array.popleft()
            else:
                print("error")
                cont = True
                break
    
    if cont: continue

    if funcRCount % 2 == 1:
        array = list(reversed(array))

    listStr = ""
    for i in array:
        listStr += str(i) + ","
    listStr = listStr.rstrip(",")

    print("[" + listStr + "]")