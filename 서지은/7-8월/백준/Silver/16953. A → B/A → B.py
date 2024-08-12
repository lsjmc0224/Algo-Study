def bfs(s, e):
    v = []  # 여기에 사용한 숫자 추가
    q = []

    # 연산 횟수를 튜플 형식으로 함께 저장
    q.append((s, 1))
    v.append(s)

    while q:
        c, cnt = q.pop(0)

        for n in (c*2, c*10+1):
            if c == e:
                return cnt

            if n<=1000_000_000 and n not in v:
                q.append((n, cnt+1))
                v.append(n)
    return -1


s, e = map(int, input().split())
ans = bfs(s, e)
print(ans)