import random
from modules import algorithms

alph = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

p_text = input("Enter plaintext data: ")

pad = []
for i in range(len(p_text)):
    x = random.choice(alph)
    pad.append(x)

p_text_num = algorithms.alph_pos(p_text)
pad_num = algorithms.alph_pos(pad)

c_text_num = []
for p in range(len(p_text_num)):
    y = (p_text_num[p] + pad_num[p]) % 26
    c_text_num.append(y)

c_text = []
for n in range(len(c_text_num)):
    for z in range(len(alph)):
        if c_text_num[n] == z:
            c_text.append(alph[z])

print("Your ciphertext encrypted with the pad:" + str("".join(pad)) + " is: " + str("".join(c_text)))
