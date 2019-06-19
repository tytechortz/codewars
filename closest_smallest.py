# def sum_string(s):
#     sum = 0
#     for digit in s:
#         sum += int(digit)
#     print(sum)
#     return sum


def closest(strng):
    totals = []
    initial_list = strng.split()
    print(initial_list)
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

        totals.append([s,i,v])

    print(totals)
    
    
# sum_string("456899 50 11992 176 272293 163 389128 96 290193 85 52")
closest("456899 50 11992 176 272293 163 389128 96 290193 85 52")