def cut(si, sj, n):
    global w_cnt, b_cnt

    color = paper[si][sj]

    for i in range(si, si+n):
        for j in range(sj, sj+n):
            if color != paper[i][j]:
                cut(si, sj, n//2)
                cut(si, sj+n//2, n//2)
                cut(si+n//2, sj, n//2)
                cut(si+n//2, sj+n//2, n//2)
                return
    if color == 0:
        w_cnt += 1
    else:
        b_cnt += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
w_cnt, b_cnt = 0, 0
cut(0, 0, N)

print(w_cnt)
print(b_cnt)