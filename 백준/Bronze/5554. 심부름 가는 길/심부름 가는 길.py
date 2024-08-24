h, m = 0, 0

for _ in range(4):
    a = int(input())
    m += a

tmp = m // 60
h += tmp
m -= (tmp*60)

print(h, m, sep="\n")