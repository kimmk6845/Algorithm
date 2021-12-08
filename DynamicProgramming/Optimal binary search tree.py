##최적 이진 탐색 트리
def optimalBST(p,a,r,n):
    for i in range(n+1):
        a[i][i] = p[i]
        r[i][i] = i
    for h in range(1,n):
        for i in range(1,n-h+1):
            j = i + h
            a[i][j] = sys.maxsize
            p_sum = 0
            for m in range(i, j+1):
                p_sum += p[m]
            for k in range(i, j+1):
                q = a[i][k-1] + a[k+1][j] + p_sum
                if q < a[i][j]:
                    a[i][j] = round(q,2)
                    r[i][j] = k

    print('A[i,j]')
    for i in range(1,n+1):
        print(a[i])
    print('K')
    for i in range(1,n+1):
        print(r[i])

    return a[1][n]

import sys
# N = 4
# P = [0.0,0.3,0.2,0.4,0.1]
N = 5
P = [0.0,0.21,0.11,0.16,0.29,0.23]  #첫 원소는 더미 키
A = []
R = []
for i in range(N+2):
    a = []
    r = []
    for i in range(N+1):
        a.append(0)
        r.append(0)
    A.append(a)
    R.append(r)
result = optimalBST(P,A,R,N)
print('최적 이진 탐색 트리 최소값: %.2f'%result)