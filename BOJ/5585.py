REAM = 1000 - int(input())
MONEY = [500, 100, 50, 10, 5, 1]
count = 0

# Greedy
for money in MONEY:
    count += REAM // money
    REAM -= money * (REAM // money)

print(count)
