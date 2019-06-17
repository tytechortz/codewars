import operator

def order_weight(string):
    mystring = ''
    answer = []
    arranged_list = []
    string = string.split()
    string = [int(i) for i in string]
    # print(len(string[0]))
    for n in string:
        s = 0
        v = n
        i = string.index(n)
        while n:
            dig = n % 10
            s += dig
            n = n//10
        # print(s)
        arranged_list.append((s,v,i))
       
        print(arranged_list)
    def sortSecond(val):
        return val[0]

    arranged_list.sort(key = sortSecond)
    # print(arranged_list)
    # print(arranged_list[0])
    for l in range(len(arranged_list)):
        print(arranged_list[l][1])
        answer.append(arranged_list[l][1])
    
    #     answer = " ".join(arranged_list[l][0])
    # print(answer)
    mystring = " ".join(map(str,answer))
    print(mystring)
   

    

order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")