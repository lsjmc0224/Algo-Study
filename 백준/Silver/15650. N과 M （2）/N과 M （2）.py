def dfs(n, s, lst):
    if n == M:
        print(*lst)
        return

    for i in range(s, N+1):
        if visited[i] == 0:
            visited[i] = 1

            lst.append(i)
            dfs(n+1, i, lst)
            lst.pop()

            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * (N+1)

dfs(0, 1, [])