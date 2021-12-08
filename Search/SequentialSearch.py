## SequentialSearch Algorithm(순차 탐색 알고리즘)
class node:
    def __init__(self, key = None):
        self.key=key

class Dict:
    def __init__(self):
        Dict.a=[]

    def search(self, search_key):
        i=0
        n = len(Dict.a)
        while i < n and (Dict.a[i].key != search_key):
            i+=1
        if i == n:
            return -1
        else:
            return i

    def insert(self, v):
        Dict.a.append(node(v))

import random,time

# key = list(range(1,10 + 1))
# s_key = list(range(1,10 + 1))
# random.shuffle(key)
# d=Dict()
# cnt = 0
# for i in range(10):
#     d.insert(key[i])
# for i in range(10):
#     result = d.search(s_key[i])
#     cnt += i
#     print("비교 횟수: ",i)
#     if result == -1 or key[result] != s_key[i]:
#         print("탐색 오류")
# print("총 비교횟수: ", cnt)
# print("비교횟수 평균 = ",cnt / 10)

### 탐색 키가 1에서 15까지인 경우
key = list(range(1,10 + 1))
s_key = list(range(1,15 + 1))
random.shuffle(key)
d=Dict()
cnt = 0
for i in range(10):
    d.insert(key[i])
for i in range(15):
    result = d.search(s_key[i])
    cnt += i
    print("비교 횟수: ", i)
    if result == -1 or key[result] != s_key[i]:
        print("탐색 오류")
print("총 비교횟수: ", cnt)
print("비교횟수 평균 = ",cnt / 15)

# N=1000
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d=Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or (key[result] != s_key[i]):
#         print("탐색 오류")
# end = time.time() - start
# print('실행시간 (N = %d) : %0.3f'%(N,end))
#
# N=2000
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d=Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or (key[result] != s_key[i]):
#         print("탐색 오류")
# end = time.time() - start
# print('실행시간 (N = %d) : %0.3f'%(N,end))
#
# N=3000
# key = list(range(1, N + 1))
# s_key = list(range(1, N + 1))
# random.shuffle(key)
# d=Dict()
# for i in range(N):
#     d.insert(key[i])
# start = time.time()
# for i in range(N):
#     result = d.search(s_key[i])
#     if result == -1 or (key[result] != s_key[i]):
#         print("탐색 오류")
# end = time.time() - start
# print('실행시간 (N = %d) : %0.3f'%(N,end))