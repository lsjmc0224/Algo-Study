N, X = map(int, input().split())
price = list(map(int, input().split()))


ans = N*X*1001
for i in range(N-1):
    total = 0
    total += price[i] * X
    total += price[i+1] * X
    ans = min(ans, total)

print(ans)