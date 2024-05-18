def incrementing_numbers():
    number = 1
    # Do 10 times
    for number in range(1,10):
        yield number

gen = incrementing_numbers()

# Example using next()
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2

for number in gen:
    print(number)