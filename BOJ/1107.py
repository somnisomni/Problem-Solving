targetChannel, M = int(input()), int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
upButtonBroken, downButtonBroken = False, False
currentChannel = 100
pressCount = 0

if M > 0:
    for broken in input().split():
        if broken.isdigit():
            buttons[int(broken)] = -1
        else:
            if broken == "+":
                upButtonBroken = True
            elif broken == "-":
                downButtonBroken = True

# Case: Initialize with single up/down count
def lengthBetween(a, b):
    return a - b if a >= b else b - a

pressCount = lengthBetween(targetChannel, currentChannel)

if pressCount == 0:
    print(0)
    exit(0)

# Case: Nearest pressable channel (brute-force)
if list(set(buttons)) != [-1]:
    upNearChannel, downNearChannel = targetChannel, targetChannel
    upNearChannelPass, downNearChannelPass = False, False

    def checkAvailable(num):
        if num < 0:
            return True

        for c in str(num):
            if buttons[int(c)] == -1:
                return False

        return True

    while upNearChannel < (500000 * 2): # Arbitrary upper limit
        if not upNearChannelPass:
            if checkAvailable(upNearChannel):
                upNearChannelPass = True
            else:
                upNearChannel += 1
        
        if not downNearChannelPass:
            if checkAvailable(downNearChannel):
                downNearChannelPass = True
            else:
                downNearChannel -= 1
        
        if upNearChannelPass and downNearChannelPass:
            break

    if not downButtonBroken:
        pressCount = min(pressCount, len(str(upNearChannel)) + lengthBetween(targetChannel, upNearChannel))

    if (downNearChannel >= 0) and (not upButtonBroken):
        pressCount = min(pressCount, len(str(downNearChannel)) + lengthBetween(targetChannel, downNearChannel))

    #print("[upNearChannel]", upNearChannel, "[downNearChannel]", downNearChannel)
print(pressCount)
