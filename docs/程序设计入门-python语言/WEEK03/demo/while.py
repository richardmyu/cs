# -*- coding: utf-8 -*-

count = 0
while count <= 5:
    print("hello")
    count += 1
print("-- 1 end--")

# continue
i = 0
j = 0
while i < 10:
    i += 1
    while j < 10:
        j += 1
        if i % 2 != 0 and j % 2 != 0:
            print("(" + str(i) + ", " + str(j) + ")")
        else:
            continue
print("--2 end--")

# break
ii = 0
jj = 0
while ii < 10:
    ii += 1
    while jj < 10:
        jj += 1
        if ii % 2 != 0 and jj % 2 != 0:
            print("(" + str(ii) + ", " + str(jj) + ")")
        else:
            break
print("--3 end--")
