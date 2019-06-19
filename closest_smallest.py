def totals(elem):
    return elem[0]



def closest(strng):
    stats = []
    initial_list = strng.split()
    # print(initial_list)
    int_list = [int(i) for i in initial_list]
    for n in int_list:
        s = 0
        v = n
        i = int_list.index(n)
        # first_digit = n[0] 
        while n:
            dig = n % 10
            s += dig
            n = n//10

        stats.append([s,i,v])

    print(stats)
    stats.sort(key=totals)
        # print(totals[x][0])\
    print(stats)

    stats.sort()

    # while i in totals < len(totals):
    #     if 
    # for lists in totals:
    #     if lists[0]
    
    
# sum_string("456899 50 11992 176 272293 163 389128 96 290193 85 52")
closest("456899 50 11992 176 272293 163 389128 96 290193 85 52")