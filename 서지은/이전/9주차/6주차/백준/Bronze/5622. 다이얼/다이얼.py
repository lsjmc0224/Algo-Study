dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j: #a[i]가 dial의 j번째 순서에 있다면 해당 j 인덱스에서 +3
            ret += dial.index(j)+3 #ABC를 누르는 데에는 3초가 걸림 dial.index(0)은 0이니까 3을 더해주는 것
print(ret)