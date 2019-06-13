def is_prime(num):
    divs = []
    answ = 0
    falses = [0,1,4]
    if num in falses or num < 0:
        return False
    else:
        for x in range(2,int(num**.5)+1):
            if x**2 <=  num:
                divs.append(x)  
        print(divs)

        for y in divs:
            if num % y == 0:
                answ += 1
    
        if answ == 0:
            return True
        else:
            return False
        

is_prime(73)