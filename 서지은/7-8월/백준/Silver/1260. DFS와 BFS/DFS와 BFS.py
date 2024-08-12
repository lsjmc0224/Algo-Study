def dfs(c):
    v1[c] = 1

    for n in adj[c]:
        if v1[n] == 0:
            ans1.append(n)
            dfs(n)


def bfs(s):
    v[s] = 1
    q = []

    q.append(s)
    ans.append(s)

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if v[n] == 0:
                v[n] = 1
                q.append(n)
                ans.append(n)


V, E, S = map(int, input().split())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

    for lst in adj:
        lst.sort()

ans1 = [S]
v1 = [0] * (V + 1)
dfs(S)
print(*ans1)

ans = []
v = [0] * (V + 1)
bfs(S)
print(*ans)