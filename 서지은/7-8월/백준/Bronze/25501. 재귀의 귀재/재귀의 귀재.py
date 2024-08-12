def palin(s):
    global cnt

    if len(s) <= 1:
        cnt += 1
        return 1

    if s[0] == s[-1]:
        cnt += 1
        return palin(s[1:-1])

    else:
        cnt += 1
        return 0


T = int(input())

for tc in range(1, T+1):
    word = input().strip()
    cnt = 0

    print(palin(word), cnt)