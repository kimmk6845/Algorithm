## AVL Tree Algorithm(AVL 트리 탐색 알고리즘)
class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class Dict:
    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0
    def search(self, search_key):
        x = self.node
        while x is not None:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, v):
        x = self.node
        if x is None:
            self.node = node(v)
            self.node.left = Dict()
            self.node.right = Dict()
        elif x.key > v:
            self.node.left.insert(v)
        else:
            self.node.right.insert(v)
        self.check_balance()

    def check_balance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                self.rotate_right()
            else:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                self.rotate_left()
            self.update_heights()
            self.update_balances()

    def rotate_right(self):
        g = self.node
        p = g.left.node
        x = p.right.node

        self.node = p
        p.right.node = g
        g.left.node = x
    def rotate_left(self):
        g = self.node
        p = g.right.node
        x = p.left.node

        self.node = p
        p.left.node = g
        g.right.node = x

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()
            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = 0

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check(self, search_key,P = None):
        x = self.node
        while x is not None:
            if x.key == search_key:
                if P == None:   #루트노트인 경우 parent가 없음
                    print("key: {}, parent: {}".format(x.key,x.key))
                else:
                    print("key: {}, parent: {}".format(x.key,P.key))
            if x.key > search_key:
                P = x
                x = x.left.node
            else:
                P = x
                x = x.right.node

import random, time

# N = 9
# key = [2,1,8,9,7,3,6,4,5]
# s_key = [1,2,3,4,5,6,7,8,9]
# d = Dict()
# for i in range(0, N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or result != s_key[i]:
#         print("탐색 오류")
# end = time.time() - start
#
# print("============================================")
# for i in range(N+1):
#     d.check(i)
# print("탐색완료")
# print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
# print("============================================")

N = 10000
print("#랜덤")
key = list(range(1,N+1))
s_key = list(range(1,N+1))
random.shuffle(key)
d = Dict()
for i in range(0,N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))

print("#정렬")
key = list(range(1,N+1))
s_key = list(range(1,N+1))
d = Dict()
for i in range(0,N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))

print("#역순")
key = list(range(N+1,1,-1))
s_key = list(range(1,N+1))
random.shuffle(key)
d = Dict()
for i in range(0,N):
    d.insert(key[i])
start = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print("탐색 오류")
end = time.time() - start
print("탐색완료")
print('탐색실행시간 (N = %d) : %0.3f'%(N,end))
