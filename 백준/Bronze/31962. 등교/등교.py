N, X = map(int, input().split())
ans = []
for i in range(1, N+1):
    S, T = map(int, input().split())
    if S+T <= X:
        ans.append(S)

if ans:
    print(ans[-1])
else: print(-1)