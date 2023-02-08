while True:
    reson = input('\nWhy do you like programming(enter q to quit): ')

    if reson != 'q':
        with open('program_reson.txt', 'a') as file_object:
            file_object.write(reson + '\n')
    else:
        break
