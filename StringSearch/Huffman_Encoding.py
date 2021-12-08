## Huffman Encoding Algorithm(허프만 인코딩)
class PQ:
    def __init__(self):
        self.heap = [0] * 100
        self.info = [0] * 100
        self.n = 0

    def insert(self,v,x):
        self.n += 1
        i = self.n
        while True:
            if i == 1:
                break
            if v >= self.heap[int(i/2)]:
                break
            self.heap[i] = self.heap[int(i/2)]
            self.info[i] = self.info[int(i/2)]
            i = int(i/2)
        self.heap[i] = v
        self.info[i] = x

    def remove(self):
        x = self.info[1]
        temp_v = self.heap[self.n]
        temp_x = self.info[self.n]
        self.n -= 1
        i = 1
        j = 2
        while j <= self.n:
            if (j < self.n) and (self.heap[j] > self.heap[j+1]):
                j += 1
            if temp_v <= self.heap[j]:
                break
            self.heap[i] = self.heap[j]
            self.info[i] = self.info[j]
            i = j
            j *= 2
        self.heap[i] = temp_v
        self.info[i] = temp_x
        return x

    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False

def index(c):
    if ord(c) == 32:
        return 0
    else:
        return (ord(c)-64)

def makeHuffman(t, m):
    for i in range(m):
        count[index(t[i])] += 1
    for i in range(27):
        if count[i]:
            pq.insert(count[i],i)
    i += 1
    while not pq.isEmpty():
        t1 = pq.remove()
        t2 = pq.remove()
        dad[i] = 0
        dad[t1] = i
        dad[t2] = -i
        count[i] = count[t1] + count[t2]
        if not pq.isEmpty():
            pq.insert(count[i],i)
        i += 1

    for k in range(27):
        i = x = 0
        j = 1
        if count[k]:
            q = dad[k]
            while q:
                if q < 0:
                    x += j
                    q = -q
                q = dad[q]
                j += j
                i += 1
        code[k] = x
        length[k] = i

def encode(t,m):
    huffman_code = ''
    for j in range(m):
        i = length[index(t[j])]
        while i > 0:
            huffman_code += str((code[index(t[j])] >> i-1) & 1)
            i -= 1
    n = len(huffman_code)
    cnt = 0
    for i in range(n):
        cnt += 1
        print(huffman_code[i], end = '')
        if cnt % 50 == 0:
            print()
    return huffman_code

def decode(t,m):
    result=''
    isbreak=False
    i=0
    while i<len(t)-1:
        temp=''
        temp=temp+t[i]+t[i+1]
        i=i+2
        while True:
            temp+=t[i]
            for j in range(len(code)):
                k = '00' + str(length[j]) + 'b'
                if temp==format(code[j],k):
                    if j==0:
                        result+=chr(32)
                        isbreak=True
                        break
                    else:
                        result+=chr(64+j)
                        isbreak=True
                        break
            i+=1
            if isbreak==True:
                isbreak=False
                break
    return result

text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION'
# text = 'A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS'
count = [0] * 100
dad = [0] * 100
length = [0] * 27
code = [0] * 27
M = len(text)
pq = PQ()
makeHuffman(text,M)
print('*****Encode*****')
E_text = encode(text,M)


#4.8 (1)번
print()
letter = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print('%-10s' % '',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(letter[k],end='\t')
print()
print('%-9s' % 'k',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(k,end='\t')
print()
print('count[k] ',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(count[k],end='\t')
print()
print('===========================================================================')

# 4.8 (2)번
print('%-9s' % 'k',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(k,end='\t')
print()
print('count[k] ',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(count[k],end='\t')
print()
print('%-8s' % 'dad[k] ',end='')
for k in range(27):
    if count[k] == 0:
        continue
    print(dad[k],end='\t')

print()
print('---------------------------------------------------------------------------')
print('%-9s' % 'k ',end='')
for k in range(27,100):
    if count[k] == 0:
        continue
    print(k,end='\t')
print()
print('count[k] ',end='')
for k in range(27,100):
    if count[k] == 0:
        continue
    print(count[k],end='\t')
print()
print('%-8s' % 'dad[k] ',end='')
for k in range(27,100):
    if count[k] == 0:
        continue
    print(dad[k],end='\t')
print()
print('===========================================================================')

#4.8 (3)번
for k in range(27):
    if k == 0:
        print('',end='\t')
        print('k',end='\t')
        print('code[k]',end=' ')
        print('length[k]',end='\t')
        print('')
    if count[k] == 0:
        continue
    print(letter[k],end='\t')
    print(k,end='\t')
    print(code[k],end='\t\t ')
    print(length[k])
print('===========================================================================')

#4.9
print('\n*****Decode*****')
D_text = decode(E_text,M)
print(D_text)