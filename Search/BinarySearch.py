## BinarySearch Algorithm(이진 탐색 알고리즘)
class node:
    def __init__(self, key = None):
        self.key = key

class Dict:
    def __init__(self):
        Dict.a = []

    def search(self,search_key):
        left = 0
        right = len(Dict.a) - 1
        while right >= left:
            mid = int((left + right) / 2)
            if Dict.a[mid].key == search_key:
                return mid
            if Dict.a[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    def insert(self, v):
        Dict.a.append(node(v))

import random, time
N = 10000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(s_key)
d = Dict()
start = time.time()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색오류')
end = time.time() - start
print('실행시간 (N = %d) : %0.3f'%(N,end))

N = 20000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(s_key)
d = Dict()
start = time.time()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색오류')
end = time.time() - start
print('실행시간 (N = %d) : %0.3f'%(N,end))

N = 30000
key = list(range(1, N + 1))
s_key = list(range(1, N + 1))
random.shuffle(s_key)
d = Dict()
start = time.time()
for i in range(N):
    d.insert(key[i])
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('탐색오류')
end = time.time() - start
print('실행시간 (N = %d) : %0.3f'%(N,end))