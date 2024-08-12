def dfs(c):
    v[c] = 1

    for n in adj[c]:
        if v[n] == 0:
            ans.append(n)
            dfs(n)


V = int(input())
E = int(input())

adj = [[] for _ in range(V+1)]  # 인접 lst 생성

for _ in range(E):
    s, e = map(int, input().split())
    # 단방향~이 아니라 양방향
    adj[s].append(e)
    adj[e].append(s)

ans = []
v = [0]*(V+1)  # visited 배열 생성
dfs(1)
print(len(ans))

