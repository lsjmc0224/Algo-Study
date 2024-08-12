T = int(input())

for _ in range(1, T+1):
    lst = list(map(str, input().strip()))

    cnt = ans = 0
    for i in range(len(lst)):
        if lst[i] == 'O':
            cnt += 1
        else:
            for k in range(1, cnt+1):
                ans += k
                cnt = 0
    for k in range(1, cnt + 1):
        ans += k
        cnt = 0

    print(ans)