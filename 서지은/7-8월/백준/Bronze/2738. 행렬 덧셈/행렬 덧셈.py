N, M = map(int, input().split())
arr_a = [list(map(int, input().split())) for _ in range(N)]
arr_b = [list(map(int, input().split())) for _ in range(N)]
arr_n = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr_n[i][j] = arr_a[i][j] + arr_b[i][j]

for lst in arr_n:
    for n in lst:
        print(n, end=" ")
    print()