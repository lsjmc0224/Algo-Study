# 2차원 배열로 받을 시  j 고정, i 만 변함

def dfs(n, s_sm, b_sm, start):
    global ans

    if n > 0:
        temp = s_sm - b_sm
        temp = abs(temp)
        ans = min(ans, temp)

    if n == N:
        return

    for i in range(start, N):
        dfs(n+1, s_sm*ingredients[i][0], b_sm+ingredients[i][1], i+1)


N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

ans = 1e9
dfs(0, 1, 0, 0)
print(ans)