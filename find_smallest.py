def smallest(n):
    sort = [int(x) for x in str(n)]
    print(sort)
    min_in = sort.index(min(sort))
    print(min_in)

smallest(261235)