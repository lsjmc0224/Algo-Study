total = 0
mx = 0
for _ in range(10):
    out, ride = map(int, input().split())
    total -= out
    mx = max(mx, total)
    total += ride
    mx = max(mx, total)

print(mx)