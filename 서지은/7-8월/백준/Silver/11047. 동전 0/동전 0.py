N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.sort(reverse=True)

ans = 0

for coin in coins:
    if K >= coin:  # K가 coin보다 클 때 (coin이 합계 값보다 크면 out)
        ans += K // coin  # 답에다가 K를 coin으로 나눈 몫을 더해줌
        K %= coin  # 그리고 K를 coin으로 나눈 나머지를 더해줌
        if K <= 0:  # 만약 K가 0보다 작아진다면 out
            break

print(ans)