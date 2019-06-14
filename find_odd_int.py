def find_it(seq):
    seq.sort()
    print(seq)
    counter = 0
    for x in range(len(seq)):
        # print(seq[x])
        if seq[x] == seq[x + 1]:
            counter += 1
            if counter % 2 == 0:
                # print(counter)
                print(seq[x])
                return seq[x]
                # break
        else:
            counter = 0


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
