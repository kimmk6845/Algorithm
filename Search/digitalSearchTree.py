## Digital Search Tree(디지털 탐색 트리 알고리즘)
class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)
# v = bitskey(11)     #11을 이진수로 변환
# print(v.bits(0, 1)) # 11의 0번 비트 출력
# print(v.bits(1, 1)) # 11의 1번 비트 출력
# print(v.bits(2, 1))

class node:
    def __init__(self,key):
        self.key = bitskey(key)
        self.left = None
        self.right = None
class Dict:
    itemMin = bitskey(0)

    z = node(itemMin)
    head = node(itemMin)
    head.left = z
    head.right = z

    def search(self,v):
        v = bitskey(v)
        x = self.head.left
        b = maxb
        self.z.key = v
        while v.get() != x.key.get():
            b = b - 1
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
        if x == self.z:
            return -1
        else:
            return x.key.get()

    def insert(self,v):
        v = bitskey(v)
        b = maxb - 1
        x = self.head.left
        p = self.head

        while x.key.get() != self.z.key.get():
            p = x
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
            b -= 1
        x = node(self.itemMin)
        x.key = v
        x.left = self.z
        x.right = self.z
        if v.bits(b+1,1):
            p.right = x
        else:
            p.left = x

    def check(self,v,P = None):
        v = bitskey(v)
        x = self.head.left
        b = maxb
        while v.get() != x.key.get():
            b = b - 1
            if v.bits(b,1):
                P = x
                x = x.right
            else:
                P = x
                x = x.left
        else:
            if P == None:
                print("key: {}, parents: {}".format(x.key.get(), x.key.get()))
            else:
                print("key: {}, parents: {}".format(x.key.get(), P.key.get()))

import random, time

N = 7
maxb = 5
key = [1,19,5,18,3,26,9]
s_key = [1,3,5,9,18,19,26]
d=Dict()
for i in range(N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("============================================")
print(key)
for i in s_key:
    d.check(i)
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
print("탐색완료")
print("============================================")

# N = 15000
# maxb = 14
# key = list(range(1,N+1))
# s_key = list(range(1,N+1))
# random.shuffle(key)
#
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))

# ## 민감도 테스트
# N = 5000
# maxb = 14
#
# print('#랜덤')
# key = list(range(1,N+1))
# s_key = list(range(1,N+1))
# random.shuffle(key)
# d1 = Dict()
# for i in range(N):
#     d1.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d1.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))

# print('#정렬')
# key = list(range(1,N+1))
# s_key = list(range(1,N+1))
# d2 = Dict()
# for i in range(N):
#     d2.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d2.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
#
# print('#역순')
# key = list(range(N,0,-1))
# s_key = list(range(1,N+1))
# d3 = Dict()
# for i in range(N):
#     d3.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d3.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))