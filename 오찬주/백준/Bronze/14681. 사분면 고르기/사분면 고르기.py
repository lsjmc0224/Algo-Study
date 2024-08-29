x = int(input())
y = int(input())

# 만약 x > 0 이면 y < 0 일땐 4, y > 0 일땐 1
# 만약 x < 0이면 y > 0일땐 2, y < 0일땐 3

if (x > 0) and ( y<0 ): print(4)
elif (x > 0) and ( y>0 ): print(1)
elif (x < 0) and ( y>0 ): print(2)
else: print(3)