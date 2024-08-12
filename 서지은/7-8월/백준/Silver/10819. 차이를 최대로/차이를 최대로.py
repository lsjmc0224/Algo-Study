# N개의 정수로 이루어진 배열 A
# 정수의 순서를 바꾸어 식의 최댓값 / 연산 후의 값은 abs로
# 정수의 크기는 -100 ~ 100
# 횟수를 세주는 n과, 최대 합계를 찾기 위한 sm / 순서가 중요하므로 P로 풀어야 함

def dfs(n, lst):
    global ans

    if n == N:
        sm = 0
        for i in range(1, N):
            sm += abs(lst[i]-lst[i-1])
        ans = max(ans, sm)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1

            dfs(n+1, lst+[nums[i]])

            visited[i] = 0


N = int(input())
nums = list(map(int, input().split()))
ans = 0
visited = [0] * (N+1)

dfs(0, [])
print(ans)