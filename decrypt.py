from modules import algorithms


c_text = input("Enter ciphertext: ")
pad = input("Enter pad: ")

c_text_num = algorithms.alph_pos(list(c_text))
pad_num = algorithms.alph_pos(list(pad))

p_text_num = []
for p in range(len(c_text_num)):
    y = algorithms.modinverse((c_text_num[p] - pad_num[p]), 26)
    p_text_num.append(y)

p_text = algorithms.num_alph(p_text_num)

print("".join(p_text))
