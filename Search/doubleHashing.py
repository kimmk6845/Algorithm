## Double Hashing(이중 해싱)
class Dict:
    def __init__(self):
        Dict.a = [-1] * M

    def search(self,v):
        x = self.hash(v)
        u = self.hash2(v)
        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]
            else:
                x = (x + u) % M
        return -1

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while Dict.a[x] != -1:
            x = (x + u) % M
        Dict.a[x] = v

    def hash(self,v):
        return v % M

    def hash2(self,v):
        return 64 - (v % 64)

    def print(self):
        for i in range(M):
            if Dict.a[i] != -1:
                print('#', end='')
            else:
                print(' ',end='')
            if (i + 1) % 60 == 0:
                print()

import random, time
# N < M
N = 10000
M = 10391
key = []
s_key = []
for i in range(N):
    r = random.randint(1,3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
print('이 때 M값: ',M)
print()
#d.print()

N = 10000
M = 21017
key = []
s_key = []
for i in range(N):
    r = random.randint(1,3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
print('이 때 M값: ',M)
print()

N = 10000
M = 31231
key = []
s_key = []
for i in range(N):
    r = random.randint(1,3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
print('이 때 M값: ',M)
print()