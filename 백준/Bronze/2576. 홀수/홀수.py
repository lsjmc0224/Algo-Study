ans = 1001
sm = 0
for _ in range(7):
    N = int(input())

    if N % 2 == 1:
        sm += N
        ans = min(ans, N)

if sm == 0:
    print(-1)
else:
    print(sm, ans, sep='\n')