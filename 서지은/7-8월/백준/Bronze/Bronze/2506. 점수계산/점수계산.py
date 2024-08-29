N = int(input())
scores = list(map(int, input().split()))

total = 0
n = 1
for i in range(N):
    if scores[i] == 1:
        total += n
        n += 1
    else:
        n = 1
print(total)