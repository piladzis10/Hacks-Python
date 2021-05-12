squares = [i**2 for i in range(1,101)]

# print(squares)

squares_8 = [i for i in squares if i % 8 == 0 ]

print(squares_8)