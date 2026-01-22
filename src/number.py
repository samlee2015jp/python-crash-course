for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)
for n in numbers:
    print(n)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
even_numbers = list(range(1, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)