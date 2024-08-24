N, M = map(int, input().split())
ans = 0

for _ in range(N):
    cnt = 0
    lst = list(map(str, input().strip()))
    if lst.count('O') > M // 2:
        ans += 1
print(ans)