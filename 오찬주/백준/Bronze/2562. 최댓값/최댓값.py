max = 0
index=0;

num =[]

for i in range(9):
  num.append(int(input()))

for i in range(9):
  if num[i] > max :
    max = num[i]
    index = i+1

print(max)
print(index)