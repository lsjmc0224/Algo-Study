lst = []
for _ in range(10):
    n = int(input())
    lst.append(n % 42)

sset = set(lst)

print(len(sset))