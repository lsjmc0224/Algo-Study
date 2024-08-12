N, M = map(int, input().split())
lst = [0]*N
for i in range(N):
    lst[i] = i+1

for _ in range(M):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]

for n in lst:
    print(n, end=" ")