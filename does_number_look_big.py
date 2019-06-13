def narcissistic( value ):
    digits = [int(x) for x in str(value)]
    length = len(digits)
    if sum(i**length for i in digits) == value:
        return True
    else:
        return False

narcissistic(153)
   