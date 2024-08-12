word = input()
#파이썬에는 reverse 함수가 존재하지 않음!
rev = word[::-1]

if word==rev:
    print(1)
else:
    print(0)