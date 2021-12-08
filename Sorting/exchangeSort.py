## exchangeSort(교환 정렬 알고리즘)
# 0번 인덱스는 더미
def exchangeSort(a,n):  # 역순으로 정렬
    for i in range(1,n):
        for j in range(i+1,n+1):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
        #print(a)

def checkSort(a,n):
    isSorted = True
    for i in range(1,n):
        if a[i] < a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

# n=6
# a=[None,3,1,2,4,6,5]
# exchangeSort(a,n)

import random, time
print("#랜덤")
n=5000
a=[None]
for i in range(n):
    a.append(random.randint(1,n))
start = time.time()
exchangeSort(a,n)
finish=time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)

print("#역순")
a=[None]
for i in range(n,0,-1):
    a.append(i)
start = time.time()
exchangeSort(a,n)
finish=time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)

print("#정렬")
start = time.time()
exchangeSort(a,n)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)