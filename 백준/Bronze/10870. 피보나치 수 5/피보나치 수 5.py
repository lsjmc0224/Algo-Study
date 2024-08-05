def solve(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    return solve(n-2) + solve(n-1)


N = int(input())
ans = solve(N)
print(ans)