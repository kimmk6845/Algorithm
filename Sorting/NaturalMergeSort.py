## Natural merge sort(자연 합병 정렬 알고리즘)
def mergeSort(l, r):
    result = []
    if type(l) == list: #런에 원소가 하나이상있는지
        if type(r) == list:
            max_i = len(l)
            max_j = len(r)
            i = 0
            j = 0
            while True:
                if l[i] > r[j]:
                    result.append(r[j])
                    j += 1
                else:
                    result.append(l[i])
                    i += 1
                if i == max_i:
                    for k in range(j,max_j):
                        result.append(r[k])
                    j = max_j
                elif j == max_j:
                    for k in range(i,max_i):
                        result.append(l[k])
                    i = max_i
                if i == max_i and j == max_j:
                    break
    return result


def NaturalMergeSort(a,n):
    run = []
    t_run = []  #런을 만들어주는 temp run
    for i in range(1,n+1):
        if a[i-1] <= a[i]:  # i번째 원소가 더 크면 런에 넣음
            t_run.append(a[i])
        elif a[i-1] > a[i]: # i번째 원소가 더 작으면 런을 분리
            run.append(t_run)
            #print("makeRun(run : {})".format(t_run))
            t_run = []  #런 초기화
            t_run.append(a[i])
    run.append(t_run)
    if (len(run) == 1):  ## 런이 하나밖에 없으면 바로 반환해줌
        return run
    idx = 0
    result = mergeSort(run[idx],run[idx+1])

    idx = 2
    while True:
        if len(result) == n:    #런을 모두 합병한 결과가 처음 리스트의 길이와 같으면 정렬 끝남
            break
        result = mergeSort(result,run[idx])
        idx += 1
    return result

import random, time
import sys
sys.setrecursionlimit(3002)

a = [-1,6,7,8,3,4,1,5,9,10,2]
b = []
b = NaturalMergeSort(a,10)
print(b)

# print('#랜덤')
# N = 1000
# a = [-1]
# for i in range(N):
#     a.append(random.randint(1, N))
# start = time.time()
# b = []
# b = NaturalMergeSort(a, N)
# finish = time.time() - start
# print('정렬하는데 걸린 시간 (N = %d) : %0.3f' % (N, finish))
#
# print('#정렬')
# N = 1000
# a = [-1]
# for i in range(N):
#     a.append(i)
# start = time.time()
# b = []
# b = NaturalMergeSort(a, N)
# finish = time.time() - start
# print('정렬하는데 걸린 시간 (N = %d) : %0.3f' % (N, finish))
#
# print('#역순')
# N = 1000
# a = [-1]
# for i in range(N,-1,-1):
#     a.append(i)
# start = time.time()
# b = []
# b = NaturalMergeSort(a, N)
# finish = time.time() - start
# print('정렬하는데 걸린 시간 (N = %d) : %0.3f' % (N, finish))
