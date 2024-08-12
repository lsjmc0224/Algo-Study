N = int(input())
lst = []

for _ in range(N):
    b = int(input())
    lst.append(b)

mx = cnt = 0
lst.reverse()

for i in range(len(lst)):
    if lst[i] > mx:
        mx = lst[i]
        cnt += 1

print(cnt)
