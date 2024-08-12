ki, qu, ro, bi, kn, pa = list(map(int, input().split()))

king = 1-ki
queen = 1-qu
rook = 2-ro
bishop = 2-bi
knight = 2-kn
pawn = 8-pa

print(king, queen, rook, bishop, knight, pawn)
