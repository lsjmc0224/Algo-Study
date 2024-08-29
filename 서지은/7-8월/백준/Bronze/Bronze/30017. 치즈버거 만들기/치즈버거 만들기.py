A, B = map(int, input().split())
ans = 0

if (A-B) == 1:
    ans = A+B
elif A <= B:
    ans = (A+A-1)
elif A > B:
    ans = (B+B+1)
print(ans)