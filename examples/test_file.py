# this
x = []
for i in range(1, 100):
    for j in range(1, 100):
        # dbg
        print("i", i)
        print("j", j)
        # /dbg
        if i % 3 == 0 and j % 3 == 0:
            print("(i, j) ", (i, j))  # _dbg
            x.append((i, j))

# should be
x = []
for i in range(1, 100):
    for j in range(1, 100):
        if i % 3 == 0 and j % 3 == 0:
            x.append((i, j))
