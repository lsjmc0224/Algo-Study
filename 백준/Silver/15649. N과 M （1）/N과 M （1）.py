def dfs(n, lst):
    if n == M:  # n이 길이가 M이 되었을 때
        print(*lst)
        return

    for i in range(1, N+1):  # 자연수이므로 1부터 N+1까지
        if visited[i] == 0:  # 중복을 허용하지 않는 순열의 경우이므로
            visited[i] = 1

            lst.append(i)  # 빈 리스트에 append
            dfs(n+1, lst)  # n+1, lst로 dfs를 돌려준 뒤
            lst.pop()  # 리스트 가장 앞에 있는 원소를 pop 해줌

            visited[i] = 0
            

N, M = map(int, input().split())
visited = [0]*(N+1)
dfs(0, [])