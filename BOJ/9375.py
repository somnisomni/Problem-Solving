###
# 예제 데이터
#   hat headgear
#   sunglasses eyewear
#   turban headgear
#
# 경우의 수 산출식 = len(headgear) * len(eyewear)는 카테고리별로 의상이 하나씩 선택된 경우만 산출된다.
#    => [(hat, sunglasses), (turban, sunglasses)]
#
# 그러므로 문제에서 요구하는 경우의 수 산출 시, 각 카테고리마다 의상이 없는 경우까지도 생각해야 한다.
# 즉, map = {
#   headgear: [hat, turban, ∅],
#   eyewear: [sunglasses, ∅]
# } 라고 생각하고 경우의 수를 산출하면 (len(headgear) + 1) * (len(eyewear) + 1)이 나온다.
#    => [(∅), (hat), (sunglasses), (turban), (hat, sunglasses), (turban, sunglasses)]
#
# 알몸의 경우(주어진 의상이 하나도 걸쳐지지 않은 경우, 즉 (∅))는 없다고 하였으므로 산출된 경우의 수 값에서 1을 뺀다.
# answer = (len(headgear) + 1) * (len(eyewear) + 1) - 1
#    => [(hat), (sunglasses), (turban), (hat, sunglasses), (turban, sunglasses)]
#
# 단순한 수학 문제였다...........
###

N = int(input())

for _ in range(N):
  M = int(input())
  WEAR = dict()

  for _ in range(M):
    _, category = input().split()
    if not category in WEAR: WEAR[category] = 0
    WEAR[category] += 1
  
  answer = 1
  for d in WEAR: answer *= WEAR[d] + 1
  answer -= 1

  print(answer)
