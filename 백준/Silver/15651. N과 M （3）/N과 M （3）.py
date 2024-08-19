'''
중복되는 수열을 여러 번 출력하면 안 되며,
사전 순으로 증가하는 순서 출력
1~N 중에 길이가 M인 수열 출력
'''
def dfs(n, lst):
    if n == M:
        print(*lst)
        return

    for i in range(1, N+1):
        lst.append(i)
        dfs(n+1, lst)
        lst.pop()

N, M = map(int, input().split())

dfs(0, [])