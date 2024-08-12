N = int(input())
lst = [int(input()) for _ in range(N)]
stk = []
ans = []
num = 1

for n in lst:
    while num <= N+1:
        if stk and stk[-1] == n:
            stk.pop()
            ans.append('-')
            break
        else:
            stk.append(num)
            num += 1
            ans.append('+')

    if num > N+1:
        print('NO')
        break

if num <= N+1:
    for n in ans:
        print(n)