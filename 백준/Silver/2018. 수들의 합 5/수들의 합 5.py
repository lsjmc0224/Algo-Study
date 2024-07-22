N = int(input())

cnt = 0
for i in range(1, N+1):
    ans = 0
    for j in range(i, N+1):
        ans += j
        if ans == N:
            cnt += 1
        elif ans > N:
            break
print(cnt)