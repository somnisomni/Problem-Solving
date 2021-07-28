N = input()
setList = [n for n in range(10)]
savedList = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
setCount = 1

def addSet():
    global setCount, setList, savedList
    setCount += 1
    
    for i in range(10):
        if setList[i] != -1:
            savedList[i] += 1
    
    setList = [n for n in range(10)]

for i in N:
    i = int(i)
    
    if i == 6 and setList[i] == -1:
        if setList[9] == -1:
            if savedList[6] > 0: savedList[6] -= 1
            elif savedList[9] > 0: savedList[9] -= 1
            else:
                addSet()
                setList[i] = -1
        else:
            setList[9] = -1
    elif i == 9 and setList[i] == -1:
        if setList[6] == -1:
            if savedList[9] > 0: savedList[9] -= 1
            elif savedList[6] > 0: savedList[6] -= 1
            else:
                addSet()
                setList[i] = -1
        else:
            setList[6] = -1
    else:
        if setList[i] == -1:
            if savedList[i] > 0:
                savedList[i] -= 1
            else:
                addSet()
        setList[i] = -1

print(setCount)