def pig_it(text):
    text = text.split()
    print(text[0][1:] + text[0][0] + 'ay')
    print(text)

pig_it('Pig latin is cool')