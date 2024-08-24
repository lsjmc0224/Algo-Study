N = int(input())

maxx, maxy = -10001, -10001
minx, miny = 10001, 10001
for _ in range(N):
    x, y = map(int, input().split())
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    minx = min(minx, x)
    miny = min(miny, y)

sm = abs(maxx-minx) * abs(maxy-miny)
print(sm)