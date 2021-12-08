##small subfile(작은 부분화일 퀵 정렬)
def insertionSort(a,l,r): #일정 크기 이하가 되면 삽입 정렬
    for i in range(l+1,r+1):
        v, j = a[i], i
        while a[j-1] > v:
            a[j] = a[j-1]
            j-=1
        a[j] = v

def quickSort(a,l,r):
    if r-l <= M:
        insertionSort(a,l,r)
    else:
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
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
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

import random, time
# N=300000
# M=15
# a=[-1]
# for i in range(N):
#     a.append(random.randint(1,N))
# start = time.time()
# quickSort(a,1,N)
# finish = time.time() - start
# print('정렬하는데 걸린 시간 : %0.3f' %finish)
# checkSort(a,N)

import sys
sys.setrecursionlimit(3002)
N=3000
M=15
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
quickSort(b,1,N)
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

# #######################################################
# ##Median of Three quickSort(중간 값 분할 퀵 정렬)
# def quickSort(a,l,r):
#     if r-l > 1:
#         mid = int((l+r)/2)
#         if a[l] > a[mid]:
#             a[l], a[mid] = a[mid], a[l]
#         if a[mid] > a[r]:
#             a[mid], a[r] = a[r], a[mid]
#         if a[l] > a[mid]:
#             a[l], a[mid] = a[mid], a[l]
#         a[mid], a[r-1] = a[r-1], a[mid]
#         v, i, j = a[r-1], l, r-1
#         while True:
#             i += 1
#             while a[i] < v:
#                 i += 1
#             j -= 1
#             while a[j] > v:
#                 j -= 1
#             if i >= j:
#                 break
#             a[i], a[j] = a[j], a[i]
#         a[i], a[r-1] = a[r-1], a[i]
#         quickSort(a, l, i-1)
#         quickSort(a, i+1, r)
#     elif a[l] > a[r]:
#         a[l], a[r] = a[r], a[l]
#
# def checkSort(a,n):
#     isSorted = True
#     for i in range(1,n):
#         if (a[i] > a[i+1]):
#             isSorted = False
#         if (not isSorted):
#             break
#     if isSorted:
#         print("정렬 완료")
#     else:
#         print("정렬 오류 발생")
#
# import random, time
# # N=300000
# # a=[None]
# # for i in range(N):
# #     a.append(random.randint(1,N))
# # start = time.time()
# # quickSort(a,1,N)
# # finish = time.time() - start
# # print('정렬하는데 걸린 시간 : %0.3f' %finish)
# # checkSort(a,N)
#
# import sys
# sys.setrecursionlimit(3002)
# N=3000
# print("# 랜덤")
# a=[None]
# for i in range(N):
#     a.append(random.randint(1,N))
# start = time.time()
# quickSort(a,1,N)
# finish = time.time() - start
# print('정렬하는데 걸린 시간 : %0.3f' %finish)
# checkSort(a,N)
#
# print("# 역순")
# # 역순
# b=[None]
# for j in range(N,0,-1):
#     b.append(j)
# start1 = time.time()
# quickSort(b,1,N)
# finish1 = time.time() - start1
# print('정렬하는데 걸린 시간 : %0.3f' %finish1)
# checkSort(b,N)
#
# print("# 정렬")
# # 정렬 된 것
# start2 = time.time()
# quickSort(a,1,N)
# finish2 = time.time() - start2
# print('정렬하는데 걸린 시간 : %0.3f' %finish2)
# checkSort(a,N)