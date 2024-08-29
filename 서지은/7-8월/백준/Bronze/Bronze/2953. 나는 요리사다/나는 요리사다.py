ans = 0
ansi = 0
for i in range(5):
    lst = list(map(int, input().split()))
    sm = sum(lst)
    ans = max(ans, sm)
    if ans == sm:
        ansi = i+1

print(ansi, ans)