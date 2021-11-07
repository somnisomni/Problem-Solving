h, m, s = map(int, input().split())
d = int(input())

time = h * (60 * 60) + m * 60 + s + d

nh = time // (60 * 60)
time -= nh * (60 * 60)
nh %= 24
nm = time // 60
time -= nm * 60
nm %= 60

print("{} {} {}".format(nh, nm, time))
