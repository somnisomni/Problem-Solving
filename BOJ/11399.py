N = int(input())
P = list(sorted(map(int, input().split())))
time = 0

# 그리디까진 아닌 것 같고 그냥 P 정렬 후 인덱스 k마다 P[0] ~ P[k]의 합을 time에 더해주면 됨
for k, _ in enumerate(P):
    time += sum(P[:k + 1])

print(time)