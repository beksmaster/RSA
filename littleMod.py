import math
import time

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

n = int(input("Введите n"))
ostatok = 11.1
i = True
k = 3
res = 3
NOD = 0
a= 0

while i == True:
    start_time = time.time()
    ostatok = n // k
    res = n /k
    check = (float(res).is_integer())
    NOD = math.gcd(ostatok, k)
    if check == False:

        k = k + 1

    if check == True :
        if NOD ==1:
            a = isPrime(ostatok)
            if a!=0:
             i = False
print("p: ",k," q: ", ostatok)
print("--- %s секунд ---" % (time.time() - start_time))
