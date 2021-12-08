##countingSort(계수 정렬 알고리즘)
def countingSort(a, n, m):
    b = [0] * (n+1)
    count = [0] * (m+1)
    for i in range(1,n+1):
        count[a[i]] = count[a[i]]+1
    for j in range(2,m+1):
        count[j] = count[j-1] + count[j]
    for i in range(n,0,-1):
        b[count[a[i]]] = a[i]
        count[a[i]] = count[a[i]]-1
    for i in range(1,n+1):
        a[i] = b[i]

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

M=1000
N=100000
a=[None]
for i in range(N):
    a.append(random.randint(1,M))
start = time.time()
countingSort(a,N,M)
finish=time.time() - start
print('10만개 정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

M=1000
N=200000
a=[None]
for i in range(N):
    a.append(random.randint(1,M))
start = time.time()
countingSort(a,N,M)
finish=time.time() - start
print('20만개 정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

M=1000
N=300000
a=[None]
for i in range(N):
    a.append(random.randint(1,M))
start = time.time()
countingSort(a,N,M)
finish=time.time() - start
print('30만개 정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)