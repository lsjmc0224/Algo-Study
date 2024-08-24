T = int(input())
n = list(map(int, input().split()))
scores = [0] * 5
total = 0

for i in range(T):
    scores[i] = n[i]

x = abs(scores[0]-scores[2])
y = abs(scores[1]-scores[3])
z = scores[4]

if scores[0] > scores[2]:
    total += x*508
else: total += x*108

if scores[1] > scores[3]:
    total += y*212
else: total += y*305

total += z*707

print(total*4763)