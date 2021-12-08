## 공개 키 암호화 시스템 (RSA 알고리즘)
def encipher(p,n,pk):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):  #십진수 평문을 4자리씩 나누기
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(pk):     # mod 계산
            b = t % n
            t = a * b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)
    return c

def decipher(p,n,sk):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(4):
            m += p[i+j]
        i += 4
        a = int(m)
        t = a
        for k in range(sk):
            b = t % n
            t = a * b
        if b < 10:
            c += '000' + str(b)
        elif b < 100:
            c += '00' + str(b)
        elif b < 1000:
            c += '0' + str(b)
        else:
            c += str(b)
    return c

def encode(p):
    m = ''
    for i in range(len(p)):
        a = ord(p[i])
        if a == 32: # space일 때는 a를 64로 만들어
            a = 64  # 00이 나오도록함
        a -= 64
        if a == 0:  # a 값이 space일 때
            m += '00'
        elif a < 10: # a값이 일의 자리일 때 앞에 0붙이도록(ABCD...HI)
            m += '0' + str(a)
        else: #나머지 문자들을 이진화
            m += str(a)
    return m

def decode(p):
    c = ''
    i = 0
    while i < len(p):
        m = ''
        for j in range(2):
            m += p[i+j]
        i += 2
        a = int(m)
        if a == 0:
            a = 32
        else:
            a += 64
        c += chr(a)
    return c

plainText = 'SAVE PRIVATE RYAN '
N = 3713
S = 97  #비밀 키
P = 37  #공개 키
plainMessage = encode(plainText)
print('평문: ',plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print('암호문: ',cipherMessage)
d_cipherMessage = decipher(cipherMessage,N,S)
print('복호문: ',d_cipherMessage)
d_Text = decode(d_cipherMessage)
print('해독문: ',d_Text)

print()

plainText = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ '
N = 3713
S = 97
P = 37
plainMessage = encode(plainText)
print('평문: ',plainMessage)
cipherMessage = encipher(plainMessage, N, P)
print('암호문: ',cipherMessage)
d_cipherMessage = decipher(cipherMessage,N,S)
print('복호문: ',d_cipherMessage)
d_Text = decode(d_cipherMessage)
print('해독문: ',d_Text)