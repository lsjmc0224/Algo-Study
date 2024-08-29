lv, com = input().split()
lv = int(lv)

if com == 'miss':
    print(0)
elif com == 'bad':
    print(lv*200)
elif com == 'cool':
    print(lv*400)
elif com == 'great':
    print(lv*600)
else:
    print(lv*1000)