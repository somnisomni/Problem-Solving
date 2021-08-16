N = int(input())
bags = 0

def solve():
    global N, bags

    # Greedy
    # 참고 : https://reakwon.tistory.com/126
    while N >= 0:
        # N // 3을 계속 빼주다가 어느 순간 N % 5가 나머지를 가지지 않는 경우 종료

        if (N % 5) == 0:
            bags += (N // 5)
            N -= 5 * (N // 5)
            break

        N -= 3
        bags += 1

solve()
print(bags if N == 0 else -1)