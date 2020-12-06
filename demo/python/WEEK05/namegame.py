# -*- coding: utf-8 -*-

f = open("./namelist.txt", "r")

print(f)

for line in f:
    print("---")
    print(line.strip().title())

f.close()
