print('Give me tow numbers, and i\'ll add them.')
print('Enter "q" to quit.')

while True:
    first_number = input("\nFirst number: ")

    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")

    if second_number == 'q':
        break

    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print('you must be enter number')
    else:
        print(sum)
