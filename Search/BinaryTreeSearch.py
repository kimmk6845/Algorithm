## BinaryTreeSearch Algorithm(이진 트리 탐색 알고리즘)
class node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x=p=node
    z=node(key=0,left=0,right=0)
    z.left = z  #null을 가리킴
    z.right = z #null
    head=node(key=0,left=0,right=z)     #head.right가 원래 노드를 가리킴

    def search(self,search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1
    def insert(self,value):
        x = p = self.head
        while x != self.z:
            p = x
            if x.key == value:
                return
            if x.key > value:
                x = x.left
            else:
                x = x.right
        x = node(key = value,left = self.z, right = self.z)
        if p.key > value:
            p.left = x
        else:
            p.right = x

# key = [2,1,7,8,6,3,5,4]
# s_key = [4]
# d = Dict()
# for i in range(len(key)):
#     d.insert(key[i])
# result = d.search(s_key[0])
# if result == -1:
#     print("탐색 오류")

import random, time
N = 10000
print("#랜덤")
key = list(range(1,N+1))
s_key = list(range(1,N+1))
random.shuffle(key)
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

print("#정렬")
key = list(range(1,N+1))
s_key = list(range(1,N+1))
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

print("#역순")
key = list(range(N+1,1,-1))
s_key = list(range(1,N+1))
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

