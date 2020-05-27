# -*- coding: utf-8 -*-

title = "Alice in Wonderland"
print(title.split())

filename = 'alice.txt'
# with open(filename) as file_object:
#     contents = file_object.read()

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("\nSorry, the file " + filename + " does not exist.")
else:
    words = contents.split()
    print(words)
    num_words = len(words)
    print("The page " + filename + " has about " + str(num_words) + " words.")
