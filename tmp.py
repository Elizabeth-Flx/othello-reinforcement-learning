


white = 2**40 + 2**49 + 2**30 + 2**21 + 2**47 + 2**12

black = 2**3 + 2**58 + 2**31


print(white)
print(black)




board = black

for i in range(8):
    for j in range(8):
        print(board >> (i*8+j) & 1, end=" ")

    print()


