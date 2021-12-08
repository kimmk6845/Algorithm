## Bubble sort(버블 정렬 알고리즘)
def BubbleSort(a,n):
    for i in range(n,0,-1):
        for j in range(1,i):    #0일때는 None값이므로 1부터
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

def checkSort(a,n):     #정렬 확인
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

import random,time
N=5000
#랜덤
print("# 랜덤")
a=[None]
for i in range(N):
    a.append(random.randint(1,N))
start = time.time()
BubbleSort(a,N)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 역순")
# 역순
b=[None]
for j in range(N,0,-1):
    b.append(j)
start1 = time.time()
BubbleSort(b,N)
finish1 = time.time() - start1
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(b,N)

print("# 정렬")
# 정렬 된 것
start2 = time.time()
BubbleSort(a,N)
finish2 = time.time() - start2
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)