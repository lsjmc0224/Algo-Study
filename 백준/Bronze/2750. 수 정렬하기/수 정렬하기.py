N = int(input())
lst = [int(input()) for _ in range(N)]

for i in range(0, N-1):
    for j in range(i+1, N):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

for i in lst:
    print(i)