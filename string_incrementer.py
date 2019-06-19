def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    print(head + str(int(tail) + 1).zfill(len(tail)))
    return head + str(int(tail) + 1).zfill(len(tail))


increment_string("foo9")