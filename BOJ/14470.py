temp = int(input())
target = int(input())
heatTimeWhenIced = int(input())
deiceTime = int(input())
heatTime = int(input())

iced = temp < 0
currentTemp = temp
elapsedTime = 0

if iced:
  elapsedTime += abs(currentTemp) * heatTimeWhenIced
  elapsedTime += deiceTime
  currentTemp = 0

elapsedTime += (target - currentTemp) * heatTime

print(elapsedTime)
