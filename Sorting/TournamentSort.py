##토너먼트
import random, time, sys

def tournamentSort(a, n):
    ## 트리 크기 계산
    L = 1
    while (True):
        if (2 ** (L - 1) >= n):
            break
        L += 1

    ## 트리 생성
    array, vector = [], []  ## 계산용 배열, 반환할 배열
    array.append(-1)  ## 계산을 편하게 하기 위해 -1을 삽입
    z = 2 ** (L - 1)  ## 트리의 윗 삼각형 크기
    tree = 2 ** (L) - 1  ## 트리 전체의 크기

    for i in range(1, z):  ## 정렬 전 트리의 빈 부분을 0으로 채움
        array.append(0)
    for i in range(1, n + 1):  ## 정렬할 배열의 값들을 집어넣음
        array.append(a[i])
    for i in range((z - 1) + n, tree):  ## 남은 부분을 0으로 채움
        array.append(0)

    ## 트리 정렬
    for j in range(1, n + 1):
        for i in range(tree - 1, 0, -2):

            if (array[i] > array[i + 1]):  ## 왼쪽 노드가 큼
                array[int(i / 2)] = array[i]
            else:
                array[int(i / 2)] = array[i + 1]  ## 오른쪽 노드가 큼

        print('top 제거 전 : ', array)
        vector.append(array[1])

        top = array[1]  ## 트리에서 가장 큰 값

        for i in range(1, 2 ** L):  ## 트리에서 가장 큰 값들을 제거
            if (array[i] == top):
                array[i] = 0
        print('top 제거 후 : ', array)
        print()
    ## 정렬된 배열 반환
    return vector

a = [-1,6,7,8,3,4,1,5,9,10,2]
b = []
b = tournamentSort(a,10)
print(b)

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