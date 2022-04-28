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

r = 0
while i == True:
    r = int(input("r? "))
    if r < n:
        if r != n:
            checkNOD = math.gcd(r, n)
            i = False
    else:
        print("Неверное значение r ")
x = pow(r, e, n)
t = modinv(r, n)
y = pow(x, C, n)
d = int(input("d? "))
w = pow(y,d,n)
M = (t*w) %n
print(M)
