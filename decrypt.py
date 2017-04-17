from modules import algorithms

c_text = input("Enter ciphertext: ")
pad = input("Enter pad: ")

c_text_num = algorithms.alph_pos(list(c_text))
pad_num = algorithms.alph_pos(list(pad))


