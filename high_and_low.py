def high_and_low(numbers):
    # ...
    nums = numbers.split()
  
    nums = list(map(int, nums))
    max_num = max(nums)
    min_num = min(nums)
    numbers = "{} {}".format(max_num,min_num)

    print(numbers)
    return numbers

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")