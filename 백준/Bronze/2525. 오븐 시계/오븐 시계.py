H, M = map(int, input().split())
CM = int(input())

CH = CM // 60
CM -= (CH*60)

H += CH
M += CM

tmp = M // 60
H += tmp
M -= tmp*60

if H >= 24:
    H -= 24
print(H, M)