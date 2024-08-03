N = int(input())
lst = list(map(int, input().split()))
oks = [-1]*N
stk = [0]

for i in range(1, N):
    while stk and lst[stk[-1]] < lst[i]:
        oks[stk.pop()] = lst[i]
    stk.append(i)
print(*oks)