def order_weight(string):
    numbers = string.split()
    print(numbers)
    split_numbers = []
    # first = numbers[0]
    for number in numbers:
        split_numbers.append([int(d) for d in number])
    # split_numbers = [int(d) for d in first]
    # print(first)
    print(split_numbers)


order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")