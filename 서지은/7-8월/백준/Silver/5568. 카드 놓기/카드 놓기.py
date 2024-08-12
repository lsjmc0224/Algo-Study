# 주어진 카드를 str으로 빈 배열에 받아 넣기
# n은 증가하는 수, word는 만들어진 수

def dfs(n, word):

    if n == K:
        sset.add(word)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1

            dfs(n+1, word+cards[i])

            visited[i] = 0


N = int(input())
K = int(input())
cards = [input() for _ in range(N)]
sset = set()
visited = [0] * (N+1)

dfs(0, '')
print(len(sset))  # set 자료형도 len 사용 가능