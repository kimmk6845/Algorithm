## Heap sort(힙 정렬 알고리즘)
def heapify(a, h, m):
    v, j = a[h], 2*h
    while j <= m:
        if j < m and a[j] < a[j+1]:
            j += 1
        if v >= a[j]:
            break
        else:
            a[int(j/2)] = a[j]
        j *= 2
    a[int(j/2)] = v

def heapSort(a, n):
    for i in range(int(n/2), 0, -1):
        heapify(a, i, n)
    for i in range(n-1, 0, -1):
        a[1], a[i+1] = a[i+1], a[1]
        heapify(a, 1, i)

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
import sys
sys.setrecursionlimit(3002)
N=3000
print("# 랜덤")
a=[None]
for i in range(N):
    a.append(random.randint(1,N))
b=a.copy()
start = time.time()
heapSort(a,N)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 역순")
# 역순
a=[None]
for j in range(N,0,-1):
    a.append(j)
b=a.copy()
start1 = time.time()
heapSort(a,N)
finish1 = time.time() - start1
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(a,N)

print("# 정렬")
# 정렬 된 것
b=a.copy()
start2 = time.time()
heapSort(a,N)
finish2 = time.time() - start2
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)