## RED-BLACK Tree Algorithm(레드-블랙트리 탐색 알고리즘)
black = 0
red = 1

class node:
    def __init__(self,color,key=None,left=None,right=None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right

class Dict:
    x=p=q=gg=node

    z=node(color=black,key=0,left=0,right=0)
    z.left=z
    z.right=z
    head=node(color=black,key=0,left=0,right=z)

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

    def check(self,N,P = None):
        x = self.head.right
        while x != self.z:
            if x.key == N:
                if P == None:  # 루트 노트인 경우 parent가 없음
                    if x.color == 1:  # 레드인 경우(숫자를 red, black으로 표기하기 위한 if문)
                        C = "red"
                        print("key: {}, parent: {}, color: {}".format(x.key, x.key, C))
                    else:  # 블랙인 경우
                        C = "black"
                        print("key: {}, parent: {}, color: {}".format(x.key, x.key, C))
                else:
                    if x.color == 1:
                        C = "red"
                        print("key: {}, parent: {}, color: {}".format(x.key, P.key, C))
                    else:
                        C = "black"
                        print("key: {}, parent: {}, color: {}".format(x.key, P.key, C))
            if x.key > N:
                P = x
                x = x.left
            else:
                P = x
                x = x.right

    def insert(self,v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return

            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)
        x = node(color=red, key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self,x,p,g,gg,v):
        x.color = red
        x.left.color = black
        x.right.color = black

        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v,g)
            x = self.rotate(v,gg)
            x.color = black
    def rotate(self,v,y):
        gc = c = node
        if y.key > v:
            c = y.left
        else:
            c = y.right

        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc
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
d=Dict()
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
d=Dict()
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
d=Dict()
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
