import math
#2.0

def chr_ascii(keyword):  # перевод из чисел в букву
    keyword = chr(keyword)
    return keyword


С = 0
length = 0
i = True
q = True
z = 0
cipher_word_keys =""




while q == True:
    C = int(input("Введите шифротекст C: "))
    n = int(input("Введите модуль n: "))
    e = int(input("Введите e: "))
    X = 1
    X = C
    while i == True:
        Y = C            # Присваиваем предыдущий ответ С
        C = pow(C, e, n) # Возводим в степень
        if X == C:
            i = False
            length = len(str(Y))
            while z <= length - 2:
                cipher_word_txt = str(Y)
                cipher_word_key = cipher_word_txt[z] + cipher_word_txt[z + 1]
                cipher_word_key_str = str(chr_ascii(int(cipher_word_key)))
                z = z + 2
                cipher_word_keys = cipher_word_keys + cipher_word_key_str
    print(cipher_word_keys)
