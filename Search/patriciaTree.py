## Patricia Tree Algorithm (패트리샤 트리 알고리즘)

maxb = 14
#maxb = 5
rootCheck = False
class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self,key):
        self.key = key
        self.b = None
        self.left = None
        self.right = None

class Dict:
    itemMin = bitskey(0)
    head = node(itemMin)
    head.b = maxb
    head.left = head.right = head

    def search(self,v):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        while p.b > x.b:
            p = x
            if self.bits(v,x.b,1):
                x = x.right
            else:
                x = x.left
        if v.get() != x.key.get():
            return self.itemMin
        return x.key

    def insert(self,v):
        v = bitskey(v)
        i = maxb
        p = self.head
        t = self.head.left
        while p.b > t.b:
            p = t
            if self.bits(v, t.b, 1):
                t = t.right
            else:
                t = t.left
        if v.get() == t.key.get() : return
        while self.bits(t.key,i,1) ==self.bits(v,i,1):
            i -= 1
        p = self.head
        x = self.head.left
        while p.b > x.b and x.b > i:
            p = x
            if self.bits(v,x.b,1):
                x = x.right
            else:
                x = x.left
        t = node(self.itemMin)
        t.key = v
        t.b = i
        if self.bits(v,t.b,1):
            t.left = x
            t.right = t
        else:
            t.left = t
            t.right = x

        if self.bits(v,p.b,1):
            p.right = t
        else:
            p.left = t

    def bits(self,item, bit, cmp):
        if item.bits(bit,1) == cmp:
            return 1
        else:
            return 0

    def check(self, v, Pa=None):
        v = bitskey(v)
        p = self.head
        x = self.head.left
        global rootCheck

        while p.b > x.b:
            p = x
            if self.bits(v, x.b, 1):
                if Pa == None:
                    if rootCheck == False:
                        print("key: {}, parents: {}".format(x.key.get(), x.key.get()))
                        rootCheck = True
                else:
                    print("key: {}, parents: {}".format(x.key.get(), Pa.key.get()))
                Pa = x
                x = x.right
            else:
                Pa = x
                x = x.left

import random, time

N = 7
key = [1,19,5,18,3,26,9]
s_key = [1,3,5,9,18,19,26]
d=Dict()
for i in range(N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result.get() == -1 or result.get() != s_key[i]:
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
#     if result.get() == -1 or result.get() != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
#
# ### 민감도 테스트
# N = 5000
#
# print('랜덤')
# key = list(range(1,N+1))
# s_key = list(range(1,N+1))
# random.shuffle(key)
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result.get() == -1 or result.get() != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
#
# print('정렬')
# key = list(range(1,N+1))
# s_key = list(range(1,N+1))
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result.get() == -1 or result.get() != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
#
# print('역순')
# key = list(range(N,0,-1))
# s_key = list(range(1,N+1))
# d = Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result.get() == -1 or result.get() != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
