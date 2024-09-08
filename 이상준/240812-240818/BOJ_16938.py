# 캠프 준비 ( https://www.acmicpc.net/problem/16938 )

# input n, l, r, x
n, l, r, x = map(int, input().split())
# input grid
grid = list(map(int, input().split()))

# 2개부터 n개까지 골라보자
count = 0
def available_prob_choose_count_when_n(
        curr_count = 0,
        idx = 0, 
        current_sum = 0, 
        max_difficulty = float('-inf'), 
        min_dificulty = float('inf')
        ):
    global count
    if idx == n:
        if curr_count >= 2:
            if l <= current_sum <= r and max_difficulty - min_dificulty >= x:
                count += 1
        return
    available_prob_choose_count_when_n(curr_count + 1, idx + 1, current_sum + grid[idx], max(max_difficulty, grid[idx]), min(min_dificulty, grid[idx]))
    available_prob_choose_count_when_n(curr_count, idx + 1, current_sum, max_difficulty, min_dificulty)

available_prob_choose_count_when_n()
print(count)