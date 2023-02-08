def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = len(contents.split())

        print(f'The file {filename} has about {str(words)} words.')


filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    count_words(file)
