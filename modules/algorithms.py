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

class ModInverse:
    def extended_gcd(self, aa, bb):
        lastremainder, remainder = abs(aa), abs(bb)
        x, lastx, y, lasty = 0, 1, 1, 0
        while remainder:
            lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
            x, lastx = lastx - quotient * x, x
            y, lasty = lasty - quotient * y, y
        return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

     def modinv(self, a, m):
        g, x, y = self.extended_gcd(a, m)
        if g != 1:
            raise ValueError
        return x % m