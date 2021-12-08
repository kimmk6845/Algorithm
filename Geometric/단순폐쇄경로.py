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

def selectionSort(p,n):
    for i in range(1, n):
        minIdx = i
        for j in range(i + 1, n + 1):
            if theta(p[1],p[j]) < theta(p[1],p[minIdx]):
                minIdx = j
        p[minIdx], p[i] = p[i], p[minIdx]

N = 12
p = []
p.append(g.point(None,None,None))
for i in range(N):
    p.append(g.point(g.x_value[i],g.y_value[i],g.c_value[i]))
minIdx = 1
for i in range(2,N+1):
    if p[i].y < p[minIdx].y:
        minIdx = i
p[minIdx],p[1] = p[1],p[minIdx]
selectionSort(p,N)
for i in range(1,N+1):
    print(p[i].c,end=' ')
print(p[1].c)