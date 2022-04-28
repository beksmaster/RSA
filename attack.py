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
print("Eve gets Bob to decipher",y)
Z = pow(y,d,n) # даем на дешифрацию
print('Bob says that the result is wrong:',Z)
#X = modinv(X,n)
P = (Z*modinv(X,n))%n
res = (P*modinv(X,n))%n
print(P)
print(res)
