x = list(input())
N = int(input())

cnt = 0
for _ in range(N):
    y = list(input())
    if x[0:5] == y[0:5]:
        cnt += 1
print(cnt)