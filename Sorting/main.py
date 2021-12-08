##자연합병
import random, time
def naturalMergeSort(a, N):
    ## 분할 단계
    b, c = [], []
    c.append(a[1])
    for i in range(2, N + 1):
        if (a[i - 1] < a[i]):  ## 작은수 -> 큰수의 형태인 경우
            c.append(a[i])
        else:  ## 큰수 -> 작은수의 형태인 경우
            b.append(c)
            c = []
            c.append(a[i])
    b.append(c)  ## 남은 부분배열 처리
    ## 합병 단계
    if (len(b[0]) == N):  ## run이 하나만 존재한다면 이미 정렬된 경우이므로 바로 반환
        return b[0]  ## 오름차순으로 이미 정렬된 배열이 들어온 경우일 것임

    result = merge(b[0], b[1])
    p = 2
    while (len(result) != N):  ## 분할한 배열들을 다 사용할 때 까지
        result = merge(result, b[p])
        p += 1

    return result


## 합병 정렬
def merge(L, R):
    result = []
    x, y = 0, 0

    while (x < len(L) and y < len(R)):
        if (L[x] >= R[y]):
            result.append(R[y])
            y += 1
        else:
            result.append(L[x])
            x += 1

    if (x != len(L)):
        for i in range(x, len(L)):
            result.append(L[i])
    if (y != len(R)):
        for i in range(y, len(R)):
            result.append(R[i])

    return result

a = [-1,6,7,8,3,4,1,5,9,10,2]
b = []
b = naturalMergeSort(a,10)

N = 1000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N - 1, -1, -1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

N = 2000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N - 1, -1, -1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

N = 3000
a = []
a.append(-1)
for i in range(N):
    a.append(random.randint(1, N))
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('임의 순서의 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('오름차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

a = []
a.append(-1)
for i in range(N - 1, -1, -1):
    a.append(i)
start_time = time.time()
b = []
b = naturalMergeSort(a, N)
end_time = time.time() - start_time
print('내림차순으로 정렬된 배열에 대한 자연합병 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))



# ##토너먼트
# import random, time, sys
#
# def tournamentSort(a, n):
#     ## 트리 크기 계산
#     L = 1
#     while (True):
#         if (2 ** (L - 1) >= n):
#             break
#         L += 1
#
#     ## 트리 생성
#     array, vector = [], []  ## 계산용 배열, 반환할 배열
#     array.append(-1)  ## 계산을 편하게 하기 위해 -1을 삽입
#     z = 2 ** (L - 1)  ## 트리의 윗 삼각형 크기
#     tree = 2 ** (L) - 1  ## 트리 전체의 크기
#
#     for i in range(1, z):  ## 정렬 전 트리의 빈 부분을 0으로 채움
#         array.append(0)
#     for i in range(1, n + 1):  ## 정렬할 배열의 값들을 집어넣음
#         array.append(a[i])
#     for i in range((z - 1) + n, tree):  ## 남은 부분을 0으로 채움
#         array.append(0)
#
#     ## 트리 정렬
#     for j in range(1, N + 1):
#         for i in range(tree - 1, 0, -2):
#
#             if (array[i] > array[i + 1]):  ## 왼쪽 노드가 큼
#                 array[int(i / 2)] = array[i]
#             else:
#                 array[int(i / 2)] = array[i + 1]  ## 오른쪽 노드가 큼
#
#         ##print('top 제거 전 : ', array)
#         vector.append(array[1])
#
#         top = array[1]  ## 트리에서 가장 큰 값
#
#         for i in range(1, 2 ** L):  ## 트리에서 가장 큰 값들을 제거
#             if (array[i] == top):
#                 array[i] = 0
#         ##print('top 제거 후 : ', array)
#         ##print()
#
#     ## 정렬된 배열 반환
#     return vector
#
#
# N = 1000
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(random.randint(1, N))
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('임의 순서의 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('오름차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N - 1, -1, -1):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('내림차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# N = 2000
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(random.randint(1, N))
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('임의 순서의 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('오름차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N - 1, -1, -1):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('내림차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# N = 3000
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(random.randint(1, N))
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('임의 순서의 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('오름차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))
#
# a = []
# a.append(-1)
# for i in range(N - 1, -1, -1):
#     a.append(i)
# start_time = time.time()
# b = []
# b = tournamentSort(a, N)
# end_time = time.time() - start_time
# print('내림차순으로 정렬된 배열에 대한 토너먼트 정렬의 실행시간 (N = %d) : %0.3f' % (N, end_time))

