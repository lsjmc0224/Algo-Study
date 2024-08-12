N, M = map(int, input().split())
lst = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        lst[n-1] = k

for n in lst:
    print(n, end=" ")