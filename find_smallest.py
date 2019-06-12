def smallest(n):
    digits = [int(x) for x in str(n)]
    length = len(digits)
    # print(length)
    sd = min(digits)
    # i = index(min(digits))
    print(sd)
    
   
    digits.reverse()
    sdi = digits.index(min(digits))
    print(sdi)

    i = length - sdi - 1
    print(i)
    # for i in rev:
    #     if 
    print(digits)
    if i == 0:
        print('hello')
        digits.remove(sd)
        print(digits)
        sd2 = min(digits)
        print(sd2)
        sdi2 = digits.index(min(digits))
        for k in digits:
            j = length - k - 1
            if sdi2 == 0:
                sd2 = min(digits)
                if sd2 < k:
                    digits.append(sd2)
                    
                    print(j)
                    
            print(digits)
            digits.reverse()
            print(digits)
            smallest = int("".join(map(str, digits)))
            print(smallest)

            answer = [smallest, i, j]
            print(answer)
            break

        
    # print(digits)
    else:
        print('fuck')
        for k in digits:
            if sdi == 0:
                sd = min(digits)
            if sd < k:
                digits.append(sd)
                j = length - k - 1
                print(j)
                break

        print(digits)
        digits.reverse()
        print(digits)
        smallest = int("".join(map(str, digits)))
        print(smallest)

        answer = [smallest, i, j]
        print(answer)
 
smallest(285365)