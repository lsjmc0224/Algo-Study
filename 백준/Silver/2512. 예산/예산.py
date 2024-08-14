def sum(m):
    ans = 0
    for cost in costs:
        ans += min(cost, m)
    return ans <= total


N = int(input())
costs = list(map(int, input().split()))
costs.sort()
total = int(input())

start = ans =  0
end = max(costs)

while start <= end:
    budget = (start+end) // 2
    if sum(budget):
        ans = budget
        start = budget + 1
    else:
        end = budget - 1
        
print(ans)