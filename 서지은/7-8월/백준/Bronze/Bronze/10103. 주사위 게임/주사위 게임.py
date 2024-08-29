chang = 100
sang = 100

N = int(input())
for _ in range(N):
    c, s = map(int, input().split())
    if c > s:
        sang -= c
    elif c < s:
        chang -= s
    else: continue

print(chang, sang, sep="\n")