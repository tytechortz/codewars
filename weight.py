def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    print(sum)
    return sum

def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    print(initial_list)
    result = " ".join(sorted(initial_list, key=sum_string))
    print(result)
    return result
   
order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")