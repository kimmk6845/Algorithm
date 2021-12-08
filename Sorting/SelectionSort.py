## Selection sort(선택 정렬 알고리즘)
def selectionSort(a, n):
    for i in range(1,n):
        minIndex = i
        for j in range(i+1,n+1):
            if a[j] < a[minIndex]:
                minIndex = j
        a[minIndex],a[i] = a[i],a[minIndex]
    return a

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
N=15000
# 랜덤
list_a=[None]
for i in range(N):
    list_a.append(random.randint(1,N))
print("# 랜덤")
start = time.time()
selectionSort(list_a,N)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(list_a,N)

# print("# 역순")
# # 역순
# list_b=[None]
# for j in range(N,0,-1):
#     list_b.append(j)
# start1 = time.time()
# selectionSort(list_b,N)
# finish1 = time.time() - start1
# print('정렬하는데 걸린 시간 : %0.3f' %finish1)
# checkSort(list_b,N)
#
# print("# 정렬")
# # 정렬 된 것
# start2 = time.time()
# selectionSort(list_a,N)
# finish2 = time.time() - start2
# print('정렬하는데 걸린 시간 : %0.3f' %finish2)
# checkSort(list_a,N)