def order_weight(string):
    mystring = ''
    answer = []
    arranged_list = []
    first_digit = []
    string = string.split()
    int_list = [int(i) for i in string]

    for numbers in string:
        first_digit.append(int(numbers[0]))
    print(first_digit)

  
    
    for n in int_list:
        s = 0
        v = n
        # first_digit = n[0] 
        while n:
            dig = n % 10
            s += dig
            n = n//10
    
        arranged_list.append((s,v))
        print(arranged_list)

    # for numbers in string:
    #     arranged_list.append()
    
    arranged_list = sorted(arranged_list, key=lambda x: (x[0], -x[1]))

    for l in range(len(arranged_list)):
        answer.append(arranged_list[l][1])
    
    mystring = " ".join(map(str,answer))
    print(mystring)
   
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")