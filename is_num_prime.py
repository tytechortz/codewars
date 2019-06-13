def is_prime(num):
    divs = []
    for x in range(3,int(num**.5)+1):
        if x**2 <  num:
            divs.append(x)  
    print(divs)

is_prime(31)