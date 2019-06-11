def isValidWalk(walk):
    #determine if walk is valid
    location_x = 0
    location_y = 0
    for i in walk:
        if i == 'n':
            location_y += 1
        elif i == 's':
            location_y -= 1
        elif i == 'e':
            location_x += 1
        elif i == 'w':
            location_x -= 1
    if len(walk) != 10 or location_x != 0 and location_y != 0:
        return False
    elif len(walk) == 10 and location_x == 0 and location_y == 0:
        return True

isValidWalk([n, s, e, w, e, s, e, w, w, s])