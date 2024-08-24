dice = list(map(int, input().split()))

total = 0
if len(list(set(dice))) == 1:
    total = 10000 + dice[0] * 1000

elif len(list(set(dice))) == 2:
    dice.sort()
    total = 1000 + dice[1] * 100

else:
    total = max(dice) * 100

print(total)