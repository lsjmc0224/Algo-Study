N = int(input())

ans = 1001
for _ in range(N):
    time_to_go, bread = map(int, input().split())

    if time_to_go <= bread:
        ans = min(ans, bread)

if ans == 1001:
    print(-1)
else:
    print(ans)