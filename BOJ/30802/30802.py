import math

n = int(input())
ts = map(int, input().split(" "))
t, p = map(int, input().split(" "))

print(sum(map(lambda x: math.ceil(x / t), ts)))
print("{} {}".format(math.floor(n / p), n % p))
