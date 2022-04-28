import math

checkNOD = 0


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
def chr_ascii(keyword):  # перевод из чисел в букву
    keyword = chr(keyword)
    return keyword

i = True
e = int(input("e? "))
C = int(input("C? "))
n = int(input("n? "))
d = int(input("d? "))
X= 0
while i == True:
    X = int(input("X? "))
    if X < n:
        if X != n:
            checkNOD = math.gcd(X, n)
            i = False
    else:
        print("Неверное значение r ")

y = (C * pow(X,e,n))%n #начальный шифр
print("Ева дает зашифровать",y)
Z = pow(y,d,n) # даем на дешифрацию
print('Боб говорит что что то не так:',Z)
#X = modinv(X,n)
P = (Z*modinv(X,n))%n
length = len(str(P))
z = 0
cipher_word_keys =""
while z  <=length-2:
    cipher_word_txt = str(P)
    cipher_word_key = cipher_word_txt[z] + cipher_word_txt[z + 1]
    cipher_word_key_str = str(chr_ascii(int(cipher_word_key)))
    z = z + 2
    cipher_word_keys = cipher_word_keys + cipher_word_key_str
print("Результат совпадает?",cipher_word_keys)
