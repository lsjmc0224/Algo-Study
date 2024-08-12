def solve():
    for k in range(min(N, M)-1, 0, -1):
        for i in range(0, N-k):
            for j in range(0, M-k):
                if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                    return k+1
    return 1

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = solve()
print(ans*ans)