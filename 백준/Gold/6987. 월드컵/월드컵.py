'''
브루트 포스로 완전 탐색 // 모든 승 무 패 경우의 수를 조합으로 생성,
백트래킹 갈겨줘야 함
'''

def dfs(n):
    global cnt
    # 세 변수의 합산이 5가 되었을 때가 가장 큰 조건
    # return 값으로 flag 반환값
    if n == 15:
        cnt = 1
        for n in res:
            if n.count(0) != 3:
                cnt = 0
                break
        return

    game1, game2 = games[n]

    for j, k in ((0, 2), (1, 1), (2, 0)):
        if res[game1][j] > 0 and res[game2][k] > 0:
            res[game1][j] -= 1
            res[game2][k] -= 1

            dfs(n+1)

            res[game1][j] += 1
            res[game2][k] += 1

ans = []
for _ in range(4):
    result = list(map(int, input().split()))
    cnt = 0
    res = []
    for i in range(0, 16, 3):
        res.append(result[i:i+3])

    games = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (2, 4), (2, 5),
            (3, 4), (3, 5),
            (4, 5)]
    dfs(0)
    ans.append(cnt)
print(*ans)