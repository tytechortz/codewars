def rgb(r, g, b):
    #your code here :)
    values = [r,g,b]
    hex_dict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    print(hex_dict[10])
    oor_values = [0 if x < 0 else 255 if x > 255 else x for x in values]
    print(oor_values)

    result = []

    for i in oor_values:
        result.append('{}{}'.format(hex_dict[int(i/16)], hex_dict[i%16]))


    # result = [str(int(i/16)) + str((i % 16) if int(i/16)<10 else hex_dict[int(i/16)] \
    # + str((i % 16) if int(i/16)<10 else hex_dict[i % 16]) for i in oor_values]
            



        # result.append("{0:0=2d}".format(int(i/16)))

    print(result) 

# def hex_conv(s):

rgb(-20,275,125)