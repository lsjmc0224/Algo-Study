N = int(input())
tops = list(map(int, input().split()))
ans = [0]*N
stk = []

for i, top in enumerate(tops):
    while stk and stk[-1][1] <= top:
        stk.pop()
    
    if stk:
        ans[i] = stk[-1][0]
        
    stk.append((i+1, top))

print(*ans, sep=" ")