def order(sentence):
    arranged = []
    sentence = sentence.split()
    x = 0
    while x < len(sentence):
        for word in sentence:
            if str(x+1) in word:
                arranged.insert(x, word)
                x+=1
    print(arranged)
    return ' '.join(arranged)

# order("4of Fo1r pe6ople g3ood th5e the2")