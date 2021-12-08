## 행렬의 연쇄적 곱셈
def matrixChaingMult(d, m, p, n):
    for h in range(1,n):
        for i in range(1, n-h+1):
            j = i + h
            m[i][j] = sys.maxsize
            for k in range(i,j):
                q = m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]
                if q < m[i][j]:
                    m[i][j] = q
                    p[i][j] = k
        if h == n-1:
            print('M')  #M 행렬 값 표 출력
            for i in range(1,n):
                for j in range(2,n+1):
                    print(m[i][j],end='\t')
                print()
            print('K')  #K 값 표 출력
            for i in range(1,n):
                for j in range(2,n+1):
                    print(p[i][j],end='\t')
                print()
    return m[1][n]  #최소 곱셈 횟수

import sys
N = 6
D = [4,2,3,1,2,2,3]
M = []
P = []
for i in range(N + 1):
    m = []
    p = []
    for i in range(N+1):
        m.append(0)
        p.append(0)
    M.append(m)
    P.append(p)
result = matrixChaingMult(D,M,P,N)
print('최소 곱셈 횟수: ',result)