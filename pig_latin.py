from string import punctuation

def pig_it(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    y = ''
    pl = []
    any(p in text for p in punctuation)
    for x in text:
        if x in punctuations:
            y = x
            text = text.replace(x, "")
            text = text.split()
    
            for word in range(len(text)):
                pl.append(text[word][1:] + text[word][0] + 'ay')
            
            return " ".join(pl) + " " + y
    else:
        text = text.split()
        for word in range(len(text)):
            pl.append(text[word][1:] + text[word][0] + 'ay')
        
        return " ".join(pl)