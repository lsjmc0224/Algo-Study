def bfs(s, e):
    q = []
    v = set()

    q.append((s, 1))
    v.add(s)

    while q:
        c, cnt = q.pop(0)
        for n in (c-1, c+1, 2*c):
            if c == e:
                return cnt-1

            if n <= 100_000 and n not in v:
                q.append((n, cnt+1))
                v.add(n)
    return -1


s, e = map(int, input().split())

ans = bfs(s, e)
print(ans)