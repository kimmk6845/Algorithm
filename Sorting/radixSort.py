##radixSort(기수 정렬 알고리즘)
def enqueue(queue,data):
    queue.append(data)
def dequeue(queue):
    if len(queue) == 0:
        print("큐가 공백")
        return -1
    else:
        data = queue.pop(0)
        return data
def digit(d,k):
    temp = 1
    for i in range(1,k):
        temp *= 10
    d = int(d/temp)
    d %= 10
    return d
def radixSort(a,n,m,queue):
    for k in range(1, m+1):
        for i in range(1,n+1):
            kd = digit(a[i], k)
            enqueue(queue[kd],a[i])
        p = 0
        for i in range(10):
            while len(queue[i]) != 0:
                p += 1
                a[p] = dequeue(queue[i])

def checkSort(a,n):
    isSorted = True
    for i in range(1,n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time
# M=5   #5번째 자리까지 있음
# N=100000
# a=[-1]
# for i in range(N):
#     a.append(random.randint(1,99999))
# Q = []
# for i in range(10):
#     Q.append([])
# start = time.time()
# radixSort(a,N,M,Q)
# finish=time.time() - start
# print('10만개 정렬하는데 걸린 시간 : %0.3f' %finish)
# checkSort(a,N)
#
# M=5
# N=200000
# a=[-1]
# for i in range(N):
#     a.append(random.randint(1,99999))
# Q = []
# for i in range(10):
#     Q.append([])
# start = time.time()
# radixSort(a,N,M,Q)
# finish=time.time() - start
# print('20만개 정렬하는데 걸린 시간 : %0.3f' %finish)
# checkSort(a,N)
#
# M=5
# N=300000
# a=[-1]
# for i in range(N):
#     a.append(random.randint(1,99999))
# Q = []
# for i in range(10):
#     Q.append([])
# start = time.time()
# radixSort(a,N,M,Q)
# finish=time.time() - start
# print('30만개 정렬하는데 걸린 시간 : %0.3f' %finish)
# checkSort(a,N)

print("# 랜덤")
M=5
N=100000
a=[-1]
for i in range(N):
    a.append(random.randint(1,99999))
start = time.time()
Q = []
for i in range(10):
    Q.append([])
radixSort(a,N,M,Q)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 역순")
# 역순
b=[-1]
for j in range(N-1,-1,-1):
    b.append(j)
Q1 = []
for i in range(10):
    Q1.append([])
start1 = time.time()
radixSort(b,N,M,Q1)
finish1 = time.time() - start1
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(b,N)

print("# 정렬")
# 정렬 된 것
Q2 = []
for i in range(10):
    Q2.append([])
start2 = time.time()
radixSort(a,N,M,Q2)
finish2 = time.time() - start2
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)