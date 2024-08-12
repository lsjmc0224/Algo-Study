w, h = map(int, input().split())
N = int(input())
r_lst = [0, h]
c_lst = [0, w]

for i in range(N):
    num, x = map(int, input().split())
    if num == 0:
        r_lst.append(x)
    else:
        c_lst.append(x)

r_lst.sort()
c_lst.sort()

r_max = c_max = 0

for i in range(1, len(r_lst)):
    r_max = max(r_max, r_lst[i] - r_lst[i-1])

for i in range(1, len(c_lst)):
    c_max = max(c_max, c_lst[i] - c_lst[i-1])

print(r_max*c_max)