cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for i in range((b-a+1)//2):
        cards[a+i], cards[b-i] = cards[b-i], cards[a+i]

for n in cards:
    print(n, end=" ")