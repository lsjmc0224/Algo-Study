def dfs(n):
    global cnt
    # depth가 15가 되었을 때 종료
    if n == 15:
        cnt = 1  # cnt를 1로 만들어주고,
        for n in res:  # 만약 입력받은 경기 결과의 승/무/패의 합계가 0이 아니라면 // -= 1 해주면서 0이 되어야 하는데 안 된 거니까
            if n.count(0) != 3:
                cnt = 0
                break
        return

    # 6개국끼리 참전하는 매치 중, home팀과 away팀의 가능한 조합을 n에 맞추어 불러와 줌
    game1, game2 = games[n]

    # 각 경기를 할 때마다 가능한 승, 무, 패 조합
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

    # 한 번에 입력받은 결과 값을 국가 단위로 쪼개서 res에 넣어줌
    for i in range(0, 16, 3):
        res.append(result[i:i+3])

    # 6개국의 가능한 매치 조합을 ... 한땀 한땀 그려봤습니다
    games = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (2, 4), (2, 5),
            (3, 4), (3, 5),
            (4, 5)]
    dfs(0)
    ans.append(cnt)
print(*ans)