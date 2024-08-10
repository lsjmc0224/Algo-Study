n = int(input())
num = list(map(int, input().split()))
total = 0

for i in num:
    fake = 0
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                fake += 1
                
        if fake == 0:
            total += 1
print(total)      