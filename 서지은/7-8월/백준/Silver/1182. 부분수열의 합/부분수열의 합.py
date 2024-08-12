def dfs(n, sm, cnt):
    global ans

    # 여기서는 특정 갯수를 뽑는 조합이 아니라
    # 갯수 상관없이 ~ N개까지 돌리면서 합이 S가 되는 부분 수열을 찾아야 함

    if n == N:
        if cnt > 0 and sm == S:
            ans += 1
        return

    dfs(n+1, sm+lst[n], cnt+1)  # 포함하는 경우와 포함하지 않는 경우
    dfs(n+1, sm, cnt)


N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

dfs(0, 0, 0)
print(ans)