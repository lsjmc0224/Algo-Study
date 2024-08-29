nums = []
for _ in range(5):
    n = int(input())
    nums.append(n)

for i in range(10):
    tmp = nums.count(i)

    if tmp >= 2:
        if tmp % 2 == 0:
            for _ in range(tmp):
                nums.remove(i)
        else:
            for _ in range(tmp-1):
                nums.remove(i)

for n in nums:
    print(n)