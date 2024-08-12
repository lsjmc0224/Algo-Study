from collections import deque

def bfs(s, g, u, d, f):
    v = set()
    q = deque()

    v.add(s)
    q.append((s, 1))

    global cnt

    while q:
        c, cnt = q.popleft()
        if s == g:
            return 0

        for n in (c + u, c - d):
            if n == g:
                return cnt

            elif n not in v and 0 < n <= f:
                q.append((n, cnt+1))
                v.add(n)
    return "use the stairs"


F, S, G, U, D = map(int, input().split())
cnt = ans = 0

ans = bfs(S, G, U, D, F)
print(ans)