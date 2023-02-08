def show_name(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

            print(contents)
    except FileNotFoundError:
        print(f'Sorry, the file {filename} does not exist.')


filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    show_name(file)
