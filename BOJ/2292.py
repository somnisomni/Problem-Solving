# 한 둘레의 마지막 숫자를 구하는 함수 f(x), 여기서 x는 중앙으로부터의 거리
#   => N이 f(x) '이내'인 경우 x 출력. 이 때 f(x)는 N과 가장 가까운 값
# f(0) = 1
# f(1) = 7     f(0) + 6
# f(2) = 19    f(1) + 12
# f(3) = 37    f(2) + 18
# f(4) = 61    f(3) + 24
### => f(x) = f(x-1) + 6 * x


N = int(input())

last = 1
x = 1
while True:
  if N <= last:
    print(x)
    break

  last += x * 6
  x += 1
