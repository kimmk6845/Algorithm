## Shell sort(쉘 정렬 알고리즘)
def shellSort(a,n):
    h=1
    while h < n:
        h = 3 * h +1
    while h > 0:
        for i in range(h+1,n+1):
            v, j = a[i], i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j -= h
            a[j] = v
        h = int(h/3)

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
a=[-1]
for i in range(N):
    a.append(random.randint(1,N))
print("Before : ",a)
start = time.time()
shellSort(a,N)
finish = time.time() - start
print("After : ",a)
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,N)

print("# 역순")
# 역순
b=[-1]
for j in range(N,0,-1):
    b.append(j)
print("Before : ", b)
start1 = time.time()
shellSort(b,N)
finish1 = time.time() - start1
print("After : ",b)
print('정렬하는데 걸린 시간 : %0.3f' %finish1)
checkSort(b,N)

print("# 정렬")
# 정렬 된 것
print("Before : ",a)
start2 = time.time()
shellSort(a,N)
finish2 = time.time() - start2
print("After : ",a)
print('정렬하는데 걸린 시간 : %0.3f' %finish2)
checkSort(a,N)