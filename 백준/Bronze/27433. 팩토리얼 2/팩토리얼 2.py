def solve(n):
    global ans

    if n > N:
        return
    solve(n+1)
    ans *= n


N = int(input())
ans = 1
solve(1)
print(ans)