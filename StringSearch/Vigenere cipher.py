## 비즈네르 암호화
def encipher(p,k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i%n]) - 64
        t = a + b
        if t > 90:
            t -= 27
        if t == 64:
            t = 32
        c += chr(t)
    return c

def decipher(p,k):
    c = ''
    n = len(k)
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 64
        b = ord(k[i%n]) - 64
        t = a - b
        if t < 64:
            t += 27
        if t == 64:
            t = 32
        c += chr(t)
    return c


plainText = 'SAVE PRIVATE RYAN'
K = 'ABC'
print('평문: ',plainText)
cipherText = encipher(plainText,K)
print('암호문: ',cipherText)
d_cipherText = decipher(cipherText,K)
print('복호문: ',d_cipherText)

print()

plainText2 = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
K = 'ABC'
print('평문: ',plainText2)
cipherText = encipher(plainText2,K)
print('암호문: ',cipherText)
d_cipherText = decipher(cipherText,K)
print('복호문: ',d_cipherText)