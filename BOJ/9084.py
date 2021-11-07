# 인터넷 검색하고 푼 문제...

def process(target, coins):
  dp = [0 for i in range(target + 1)]
  dp[0] = 1

  for coin in coins:
    for i in range(coin, target + 1):
      dp[i] += dp[i - coin]

  return dp[target]

for _ in range(int(input())):
  _ = input()
  coins = list(map(int, input().split()))
  target = int(input())

  print(process(target, coins))
