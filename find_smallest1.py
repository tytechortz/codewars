def smallest(n):
    all_digits = [int(x) for x in str(n)]
    digits = [int(x) for x in str(n)]
    length = len(all_digits)
    # print(length)
    sd = min(all_digits)
    # i = index(min(digits))
    print(sd)
    sdi = all_digits.index(min(all_digits))
    print(sdi)
    if sdi == 0:
        j = 0
        digits.remove(sd)
        print(digits)
        sd2 = min(digits)
        i2 = digits.index(min(digits)) + 1
        print(sd2)
        print(i2)
        # digits = all_digits
        print(digits)
        digits.remove(sd2)
        print(digits)
        digits.reverse()
        print(digits)
        print('shit')
       
        # index = 0
        for k in digits:
            
            if sd2 < k:
                digits.append(sd2)
                
                print(j)
                print(digits)
                digits.append(sd)
                print(digits)
                digits.reverse()
                print(digits)
                smallest = int("".join(map(str, digits)))
                print(smallest)
                answer = [smallest, i2, 1]
                print(answer)
                j += 1
                return answer
             

    else:
        i = digits.index(min(digits))
        print(i)
        print('fuck')
        print(digits)
        digits.remove(sd)
        print(digits)
        for k in digits:
            if sd < k:
                j = 0
                print(digits)
                digits.insert(j,sd)
                print(j)
                print(digits)
                smallest = int("".join(map(str, digits)))
                print(smallest)
                answer = [smallest, i, j]
                print(answer)
                return answer
              
            else: j += 1
               
                      
smallest(209917)