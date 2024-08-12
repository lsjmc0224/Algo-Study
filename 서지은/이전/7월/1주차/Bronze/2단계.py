#1330

a, b = map(int, input().split())

if a>b:
    print('>')

elif a==b:
    print('==')

else:
    print('<')


#9498

s = int(input())

if s>=90:
    print('A')
elif s>=80:
    print('B')
elif s>=70:
    print('C')
elif s>=60:
    print('D')
else:
    print('F')

