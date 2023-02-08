magicians = ['bob', 'kevin', 'stuart']


def show_magicians(items):
    for item in items:
        print(item)


def make_great(items):
    for item in items:
        items[items.index(item)] = 'the Great ' + item


make_great(magicians)
show_magicians(magicians)
