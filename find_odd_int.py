def find_it(seq):
    for x in seq:
        if seq.count(x) % 2 != 0:
            print(x)
            return x
find_it([-2, -2,-1,-1,1])
