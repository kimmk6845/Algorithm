## Quick sort(퀵 정렬 알고리즘)
def quickSort(a, l ,r):
    if r > l:
        v, i, j = a[r], l-1, r
        while True:
            i += 1
            while a[i] < v:
                i += 1
            j -= 1
            while a[j] > v:
                j -= 1
            if i >= j:
                break
            a[i],a[j] = a[j],a[i]
        a[i],a[r] = a[r],a[i]
        quickSort(a, l, i - 1)
        quickSort(a, i + 1, r)

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


# a=[-1,7,4,8,2,9,1,3,10,5,6]
# quickSort(a,1,10)



import random, time
import sys
sys.setrecursionlimit(3002)
N=3000
print("# 랜덤")
a=[-1]
for i in range(N):
    a.append(random.randint(1,N))
start = time.time()
quickSort(a,1,N)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 역순")
# 역순
b=[-1]
for j in range(N,0,-1):
    b.append(j)
start1 = time.time()
quickSort(a,1,N)
finish1 = time.time() - start1
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(b,N)

print("# 정렬")
# 정렬 된 것
start2 = time.time()
quickSort(a,1,N)
finish2 = time.time() - start2
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)
