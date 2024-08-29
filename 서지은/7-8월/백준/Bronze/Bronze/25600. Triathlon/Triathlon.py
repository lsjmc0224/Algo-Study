N = int(input())
ans = 0
maxi = 0

for i in range(N):
    a, d, g = map(int, input().split())
    score = a * (d+g)
    if a == (d+g):
        score *= 2
    ans = max(ans, score)
print(ans)