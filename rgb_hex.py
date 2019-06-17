def rgb(r, g, b):
    #your code here :)
    values = [r,g,b]
    oor_values = [0 if x < 0 else 255 if x > 0 else x for x in values]

    print(oor_values)    


rgb(-10,0,300)