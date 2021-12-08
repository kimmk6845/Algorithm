##단순 암호화 기법 2. 문자변환표
def encipher(p,k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32:
            a = 0
        else:
            a -= 64
        c += k[a]
    return c

def decipher(p,k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        if chr(a) == k[0]:   #k의 0번째 값이면
            a = 32  #space값으로
        else:
            for j in range(len(k)):
                if p[i] == k[j]:
                    a = j + 64
        c += chr(a)
    return c

plainText = 'SAVE PRIVATE RYAN'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평문: ',plainText)
cipherText = encipher(plainText,K)
print('암호문: ',cipherText)
d_cipherText = decipher(cipherText,K)
print('복호문: ',d_cipherText)

print()

plainText2 = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
K = 'QHCBEJKARWSTUVD IOPXZFGLMNY'
print('평문: ',plainText2)
cipherText = encipher(plainText2,K)
print('암호문: ',cipherText)
d_cipherText = decipher(cipherText,K)
print('복호문: ',d_cipherText)