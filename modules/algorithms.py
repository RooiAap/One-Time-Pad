def alph_pos(text):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = []

    for i in range(len(text)):
        for p in range(len(alph)):
            if text[i] == alph[p]:
                x = p + 1
                l.append(x)

    return l

def euclidean(x, y):
    while 1:
        z = x % y
        if z == 0:
            break
        x = y
        y = z
    
    return y