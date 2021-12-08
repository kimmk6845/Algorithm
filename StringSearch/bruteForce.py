## Brute-Force Algorithm(직선적 알고리즘)
def bruteForce(p,t,k):
    M = len(p)
    N = len(t)
    i = k
    j = 0
    while i < N and j < M:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i

text = '00001010101011101010'
pattern = '11010'
M = len(pattern)
N = len(text)
k = 0
while True:
    pos = bruteForce(pattern, text,k)
    k = pos + M
    if k < N:
        print('패턴이 나타난 위치:',pos)
    else:
        break
print('스트링 탐색 종료')