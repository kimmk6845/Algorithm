### KMP Algorithm(KMP 탐색 알고리즘)
# def initNext(p):    #next 배열(재시작 위치)구하는 함수
#     M = len(p)
#     next[0] = -1
#     i = 0
#     j = -1
#     while i < M:
#         next[i] = j
#         while j >= 0 and p[i] != p[j]:
#             j = next[j]
#         i += 1
#         j += 1

def initNext(p):    #개선된 유한장치 도입
    M = len(p)
    next[0] = -1
    i = 0
    j = -1
    while i < M:
        if j != -1 and p[i] == p[j]:
            next[i] = next[j]
        else:
            next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

next = [0] * 9
pattern = 'abcabcabc'
M = len(pattern)
initNext(pattern)
for i in range(1, M):
    print(next[i],end=' ')