import math
import time
start_time = time.time()
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

while i == True:
    ostatok = n // k
    res = n /k
    check = (float(res).is_integer())
    NOD = math.gcd(ostatok, k)
    if check == False:

        k = k + 1
        print(k)

    if check == True :
        i = False
print("p: ",k," q: ", ostatok)
print("--- %s seconds ---" % (time.time() - start_time))
