N = int(input())
not_cute = 0
yes_cute = 0

for _ in range(N):
    cute = int(input())
    if cute == 0:
        not_cute += 1
    else:
        yes_cute += 1

if not_cute > yes_cute:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")