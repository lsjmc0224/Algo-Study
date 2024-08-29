science = [int(input()) for _ in range(4)]
society = [int(input()) for _ in range(2)]

science.sort(reverse=True)
society.sort(reverse=True)

sc_mx = sum(science) - science[3]
so_mx = society[0]

print(sc_mx + so_mx)