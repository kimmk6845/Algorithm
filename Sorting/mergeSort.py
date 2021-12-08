## merge sort(합병 정렬 알고리즘)
def mergeSort(a, l, r):
    if r > l:
        mid = int((r+l)/2)
        mergeSort(a, l, mid)
        mergeSort(a, mid+1, r)
        for i in range(mid+1, l, -1):
            b[i-1] = a[i-1]
        i -= 1
        for j in range(mid, r):
            b[r+mid-j] = a[j+1]
        j += 1
        for k in range(l, r+1):
            if b[i] < b[j]:
                a[k] = b[i]
                i += 1
            else:
                a[k] = b[j]
                j -= 1

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
#랜덤
print("# 랜덤")
a=[None]
for i in range(N):
    a.append(random.randint(1,N))
b=a.copy()
start = time.time()
mergeSort(a, 1, N)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 정렬")
# 정렬 된 것
b=a.copy()
start2 = time.time()
mergeSort(a, 1, N)
finish2 = time.time() - start2
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)

print("# 역순")
# 역순
a=[None]
for j in range(N,0,-1):
    a.append(j)
b=a.copy()
start1 = time.time()
mergeSort(a, 1, N)
finish1 = time.time() - start1
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(a,N)

