# N*N개의 체스판 위의 퀸 N개
# 퀸은 다른 기물이 막고 있지 않는 이상 상하좌우, 대각선 어디든 이동이 가능함
# 이동 시 칸 수에 제한은 없음
# 한 행에 말은 하나씩 위치해야 함, 8방 탐색 시 visited==0일 시 cnt += 1

def dfs(n):
    global res

    if n == N:
        res += 1
        return

    # v1 ~ v3까지 모두 0일 때로 기준을 잡아야 함

    for i in range(N):
        if visited_1[i] == 0 and visited_2[n+i] == 0 and visited_3[n-i] == 0:
        # if visited_1[i] == visited_2[n+i] == visited_3[n-i] == 0:
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = 1
            dfs(n+1)
            visited_1[i] = visited_2[n+i] = visited_3[n-i] = 0

N = int(input())
visited_1, visited_2, visited_3 = [[0] * (2*N) for _ in range(3)]
res = 0

dfs(0)
print(res)