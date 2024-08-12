N = int(input())
lst = []

for _ in range(N):
    t = int(input())
    lst.append(t)

cnt_l = cnt_r = mx_l = mx_r = 0
lst_a = list(reversed(lst))

for i in range(N):
    if lst[i] > mx_l:
        mx_l = lst[i]
        cnt_l += 1
    if lst_a[i] > mx_r:
        mx_r = lst_a[i]
        cnt_r += 1

print(cnt_l)
print(cnt_r)
