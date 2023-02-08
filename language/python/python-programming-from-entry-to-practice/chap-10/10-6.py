print('Give me tow numbers, and i\'ll add them.')
print('Enter "q" to quit.')

first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")

try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print('you must be enter number')
else:
    print(sum)
