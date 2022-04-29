import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
i=0
def modinv(a, m): #Нахождение инверсии по модулю
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def chr_ascii(keyword):  # перевод из чисел в букву
    keyword = chr(keyword)
    return keyword

def isPrime(n): #Проверка на простоту
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def ordin_ascii(keyword):  # перевод из букв в ascii
    keyword = ord(keyword)
    return keyword

c = True
while c ==True:
    x = 0
    while x != 1:
        word = input("Word?:  ")
        a = False
        q = 0
        NOD = 1
        i = True
        while 0 == a:
            p = int(input("p? "))
            a = isPrime(p)
            print(a)
        a = False
        while 0== a:
            q = int(input("q? "))
            a = isPrime(q)
            print(a)
        print("p: ", p, " q:", q)
        n = p * q
        f = (p - 1) * (q - 1)
        print("n: ", n, " f(", n, "): ", f)
        while i == True:
            e = int(input("e?:"))
            if (1 < e < f):
                check = math.gcd(e, f)
                if (check == 1):
                    NOD = modinv(e, f)
                    if NOD != 0:
                        if NOD != e:
                            i = False
                            d = NOD
                            print("Секретный ключ d, найден", d)
            else:
                print("Неверное значение e, секретный ключ не найден")

        x = 1

    length = len(word)
    i = length - 1
    cipher_word = ''
    otvet = 0

    while i >= 0:  # цикл для
        word = word.upper()
        cipher = ordin_ascii(word[i])
        i = i - 1
        cipher_word = str(cipher) + cipher_word
        # print(cipher)
        cipher_word_int = int(cipher_word)

    print("Исходный текст", cipher_word)
    cipher_word_int = pow(cipher_word_int,e,n) #Шифруем текст
    print("Зашифрованный текст", cipher_word_int)
    cipher_word_keys =""
    z = 0
    cipher_word_int = pow(cipher_word_int, d, n) #Расшифровываем текст
    print(cipher_word_int)
    length = len(str(cipher_word_int))
    while z  <=length-2:
        cipher_word_txt = str(cipher_word_int)
        cipher_word_key = cipher_word_txt[z] + cipher_word_txt[z+1]
        cipher_word_key_str = str(chr_ascii(int(cipher_word_key)))
        z= z+2
        cipher_word_keys = cipher_word_keys+ cipher_word_key_str
    print("Расшифрованный текст", cipher_word_keys)