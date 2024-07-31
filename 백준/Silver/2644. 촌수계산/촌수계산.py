def bfs(s, G):
    v = [0] * (V+1)
    q = []

    v[s] = 1
    q.append(s)

    while q:
        c = q.pop(0)

        if c == G:
            return v[c]-1

        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c]+1
    return -1


V = int(input())
S, G = map(int, input().split())
E = int(input())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    e, s = map(int, input().split())  # 앞에 받는 수가 뒤에 받는 수의 부모이므로 바꿔서 받아줌
    adj[s].append(e)
    adj[e].append(s)

ans = bfs(S, G)
print(ans)

