N = int(input())
score = list(map(int, input().split()))
ans = 0
maxi = max(score)

for i in range(N):
    score[i] = score[i] / maxi * 100
    ans += score[i]

print(ans / N)
