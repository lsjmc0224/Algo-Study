# 겉넓이 구하기 https://www.acmicpc.net/problem/16931
'''
교훈
1. 똥꼬쇼 말고 패딩해라
'''

# n, m 받아옴 
n, m = map(int, input().split())

# 도형 그리드 받아옴
grid = [list(map(int, input().split())) for _ in range(n)]

# 겉넓이 구하기
def gutnulbi(n, m, grid):
    count = 0
    # 동쪽
    for row in range(n):
        for col in range(m):
            if col == m-1:
                count += grid[row][col]
            else:
                count += max(grid[row][col] - grid[row][col + 1], 0)
    # 서쪽
    for row in range(n):
        for col in range(m):
            if col == 0:
                count += grid[row][col]
            else:
                count += max(grid[row][col] - grid[row][col - 1], 0)
    # 남쪽
    for row in range(n):
        for col in range(m):
            if row == 0:
                count += grid[row][col]
            else:
                count += max(grid[row][col] - grid[row - 1][col], 0)
    # 북쪽
    for row in range(n):
        for col in range(m):
            if row == n-1:
                count += grid[row][col]
            else:
                count += max(grid[row][col] - grid[row + 1][col], 0)
    # 상하방향
    count += 2 * n * m
    return count

print(gutnulbi(n, m, grid))