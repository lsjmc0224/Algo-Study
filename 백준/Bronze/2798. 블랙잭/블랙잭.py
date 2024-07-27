n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst_1 = []

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sm = lst[i] + lst[j] + lst[k]
            if sm > m:
                continue
            else:
                lst_1.append(sm)
print(max(lst_1))
