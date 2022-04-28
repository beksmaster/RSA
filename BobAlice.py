# https://asecuritysite.com/encryption/c_c
e=343
d=12007
N=158400
r=343
M=7879
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
i=0
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

cipher=pow(M,e,N)
print ('==Initial values ====')
print ('e=',e,'d=',d,'N=',N)
print ('message=',M,'r=',r)
print ('\n=============')

print ('\nInitial cipher:\t',cipher)

cipher_dash = (cipher * pow(r,e , N)) % N
print ('Eve gets Bob to decipher:\t',cipher_dash)


decipher = pow(cipher_dash,d , N)

print ('Bob says that the result is wrong:',decipher)

res = (decipher * modinv(r,N)) % N

print ('Eve determines as:',res)

if (res==M):
	print ('Eve has cracked message, as result is same as message')
else:
	print ('Eve has not cracked the message')