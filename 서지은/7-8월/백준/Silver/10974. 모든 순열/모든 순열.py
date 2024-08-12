def dfs(n, lst):
    if n == N:
        print(*lst)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            
            lst.append(i)
            dfs(n+1, lst)
            lst.pop()
            
            visited[i] = 0


N = int(input())
visited = [0] * (N+1)

dfs(0, [])