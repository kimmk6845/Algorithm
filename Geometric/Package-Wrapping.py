## 짐꾸리기 알고리즘
import geo as g

def theta(p1,p2):
    dx = p2.x - p1.x
    ax = abs(dx)
    dy = p2.y - p1.y
    ay = abs(dy)
    if ax + ay == 0: t = 0
    else: t = dy/(ax+ay)
    if dx < 0: t = 2-t
    elif dy < 0: t = 4+t
    return t * 90

def packageWrapping(p,n):
    minidx = 0
    for i in range(n):
        if p[i].y < p[minidx].y:
            minidx = i
    p[n] = p[minidx]
    th = 0.0
    for m in range(n):
        p[m],p[minidx] = p[minidx],p[m]
        minidx = n
        v = th
        th = 360.0
        for i in range(m+1,n+1):
            if theta(p[m],p[i]) > v:
                if theta(p[m],p[i]) < th:
                    minidx = i
                    th = theta(p[m],p[minidx])
                if minidx == n:
                    return m
#연습문제 5.3
N = 12
p = []
for i in range(N):
    p.append(g.point(g.x_value[i],g.y_value[i],g.c_value[i]))
p.append(g.point(None,None,None))
M = packageWrapping(p,N)
for i in range(M+1):
    print(p[i].c,end = ' ')
