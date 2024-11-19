# 인구이동 ( https://www.acmicpc.net/problem/16234 )

from collections import deque

# n, l, r, 초기 인구, 초기 연합
n, l, r = 2, 20, 50
grid_pop = [[50, 30], [20, 40]]
grid_yeonhap = [[0, 0], [0, 0]]
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# 국경열기
def open_border(grid_pop, grid_yeonhap, r, c, int_yeonhap_num):
    print(grid_pop)
    temp_grid_yeonhap = [row[:] for row in grid_yeonhap]
    queue = deque([(r, c)])
    temp_grid_yeonhap[r][c] = int_yeonhap_num
    
    while queue:
        v = queue.popleft()
        print(v)
        for dr, dc in dirs:
            nxt_r, nxt_c = v[0] + dr, v[1] + dc
            print(nxt_r, nxt_c)
            print(temp_grid_yeonhap)
            print(abs(grid_pop[v[0]][v[1]] - grid_pop[nxt_r][nxt_c]))
            if (0 <= nxt_r < n and 0 <= nxt_c < n and
                temp_grid_yeonhap[nxt_r][nxt_c] == 0 and
                l <= abs(grid_pop[v[0]][v[1]] - grid_pop[nxt_r][nxt_c]) <= r):
                print(abs(grid_pop[v[0]][v[1]] - grid_pop[nxt_r][nxt_c]))
                queue.append((nxt_r, nxt_c))
                temp_grid_yeonhap[nxt_r][nxt_c] = int_yeonhap_num
    
    return temp_grid_yeonhap

result = open_border(grid_pop, grid_yeonhap, 0, 0, int_yeonhap_num=1)
print(result)
print(grid_yeonhap)  # 원본이 변경되지 않았는지 확인

# 인구이동 
# def pop_move(grid_pop, grid_yeonhap):
#     if 

# 연합 만들기 

# 각 연합에서 이동이 일어났는가?

# 각 나라의 인구는 연합 평균이 됨 (int 형)

# 국경선 닫기