arr = []

for _ in range(3):
    arr.append(int(input()))
    
arr.sort()
    
if arr[0]+arr[1]+arr[2] == 180:
    if arr[0]==arr[1]==arr[2]:
        print('Equilateral')
    elif arr[0]==arr[1] or arr[1]==arr[2]:
        print('Isosceles')
    elif arr[0]!=arr[1] and arr[1]!=arr[2]:
        print('Scalene')
else:
    print('Error')